import redis 
import os 
import json
from redis import Redis

REDIS_HOST = os.getenv("REDIS_HOST","localhost")
REDIS_PORT = os.getenv("REDIS_PORT","6379")

producer = redis.Redis(host=REDIS_HOST, port=REDIS_PORT,db=0,decode_responses=True)


def get_data_from_file():
    with open("data/border_alerts.json",'r') as file:
        data = json.load(file)
    return data

def insert_to_queue(data:list[dict], producer:Redis):
    try:
        for alert in data:    
            alert = json.dumps(alert).encode()

            if alert['priority'] == 'URGENT':
                producer.lpush("urgent_queue",alert)
            elif alert['priority'] == 'NORMAL':
                producer.lpush("normal_queue:1",alert)
            
    except Exception as e:
        print(f' failed insertion to queue {e}')
