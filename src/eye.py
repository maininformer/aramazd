import imagehash
from PIL import Image
from py2neo import Graph, Node, Relationship
import redis

graph = Graph("http://neo4j:password@neo4j:7474/db/data/")
redis = redis.StrictRedis(host='redis', port=6379, db=0)

hash = imagehash.whash(Image.open('./images/purple.jpg'))
other_hash = imagehash.whash(Image.open('./images/yellow.jpg'))

redis.set("purple", hash)
image = Node("Visual", image_hash_redis_key="purple")

print(redis.get("purple"))

