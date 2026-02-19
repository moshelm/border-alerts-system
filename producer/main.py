from connection_redis import get_data_from_file, insert_to_queue, producer 
from priority_logic import sorting_alerts

def main():
    data = get_data_from_file()
    sorting_alerts(data)
    insert_to_queue(data, producer)
if __name__=="__main__":
    main()
