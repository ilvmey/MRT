from message_queue.base import conn, OriginDestinationConsumer, od_data_queue

if __name__ == '__main__':
    worker = OriginDestinationConsumer(conn, od_data_queue.routing_key)
    worker.run()