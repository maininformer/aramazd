from PIL import Image
import imagehash
hash = imagehash.whash(Image.open('./images/purple.jpg'))
other_hash = imagehash.whash(Image.open('./images/yellow.jpg'))

from py2neo import Graph, authenticate

graph = Graph("http://neo4j:pass@neo4j:7474/db/data/")
