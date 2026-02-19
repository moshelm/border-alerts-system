import connection_mongo as mongo
from connection_redis import consumer
from redis import Redis
from datetime import datetime
import json

def pop_from_queues(consumer:Redis):
    while True:
        queue,data = consumer.blpop(["urgent_queue"])
        if not data:
            queue, data = consumer.blpop(["normal_queue"])
        
        data = json.loads(data).encode()
        data['insertion_time'] = datetime.now()
        
        insert_to_mongo(data)

def insert_to_mongo(data:dict):
    mongo.collection.insert_one(data)

def main():
    pop_from_queues(consumer)

if __name__=="__main__":
    main()