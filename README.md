* `docker-compose up'
* Visit localhost:7474; enter password: `neo4j` and change it to `password` when prompted
* `docker-compose run python bash`

Usefull commands:

* redis: flushall
* neo4j: MATCH (n)-[r:`ASSOCIATED WITH`]->()
DELETE r , match (n) return n;

# TODOS
* It might be good to not put sounds in the same node as an image so that the meanings can change over time, e.g. what if the first time the brain sees red it hears green; or what if someone lies to it, it needs to be able to correct itself by others repeatedly showing red and saying "red". I believe that can be achieved by weakening the link between the sound green and the color red and strenghtening the link betweeh the sound red and the image green 
