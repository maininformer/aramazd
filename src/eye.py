from PIL import Image
import imagehash
hash = imagehash.whash(Image.open('./images/purple.jpg'))
other_hash = imagehash.whash(Image.open('./images/yellow.jpg'))
print(hash-other_hash)
