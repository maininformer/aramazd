import imagehash
from PIL import Image
from uuid import uuid4

from brain import Brain

class Eye(Brain):
    def __init__(self):
        super(Eye, self).__init__()

    def see(self, image_location):
        name = uuid4()
        # open the image and hash it
        hash = imagehash.whash(self.__open(image_location))
        # look up the image by hash and return similar ones
        key_and_similarity = self.__lookup_by_hash(type_='Visual', hash=hash)
        if len(key_and_similarity) > 0:
            # two for loops because we need
            # to make sure this is not a repeat node
            # first, i.e. having yellow, purple while
            # seeing purple again will create a duplicate
            # yellow-purple, whilse purple, yellow will
            # not, this two step for loop will prevent
            # that
            for entry  in key_and_similarity:
                if entry['similarity'] == 0:
                    # if it is the same, it is recorded
                    # and associated before (this will be
                    # dependent on the the precision of recognition
                    return None
            for entry in key_and_similarity:
                # TODO: only associate similarities within a threshold
                # decode utf-8 cause redis returns byte string like b'Visual ...' and
                # that throws in querying neo4j
                found_neighbor = self.find_neighbor(('redis_key', entry['key'].decode('utf-8')))
                self.record(name, 'Visual', hash, image_location, neighbor=found_neighbor, link=entry['similarity'])
        else:
            self.record(name, 'Visual', hash, image_location)


    def __lookup_by_hash(self, type_, hash):
        def diff(this, another):
            return abs(this-another)/len(another.hash)**2
        key_and_similarity = []
        results = self.lookup_by(type_)
        for result in results:
            key_and_similarity.append({
                'key': result['key'],
                'similarity': diff(hash, imagehash.hex_to_hash(result['value']))})
        return key_and_similarity

    def __open(self, image_location):
        return Image.open(image_location)

