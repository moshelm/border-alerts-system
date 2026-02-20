import connection_mongo as mongo
from connection_redis import consumer
from redis import Redis
from datetime import datetime
import json

def pop_from_queues(consumer:Redis):
    queues = ["urgent_queue","normal_queue"]
    num =0 
    while True:
        queue, data = consumer.blpop(["urgent_queue","normal_queue"])    
        data = json.loads(data)
        data['insertion_time'] = datetime.now().astimezone()
        insert_to_mongo(data)

def insert_to_mongo(data:dict):
    mongo.collection.insert_one(data)

def main():
    pop_from_queues(consumer)

if __name__=="__main__":
    main()