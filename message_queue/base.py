import json
import os
import time

import django
from kombu import Connection, Producer, Exchange, Queue
from kombu.mixins import ConsumerMixin
import pymongo

from misc.data_path import MRT_RAW_DATA_PATH
from utils.data_processor import convert_csv_to_json
from utils.mongodb_client import get_client

django.setup()

from mrt_app.models import MRTResource



USERNAME = os.getenv('RABBITMQ_DEFAULT_USER')
PASSWORD = os.getenv('RABBITMQ_DEFAULT_PASS')
HOST = os.getenv('RABBITMQ_HOST', 'localhost')
PORT = os.getenv('RABBITMQ_PORT', 5672)
exchange = Exchange('mrt', type='direct')
conn = Connection(f'amqp://{USERNAME}:{PASSWORD}@{HOST}:{PORT}//')
producer = Producer(conn)

od_data_queue = Queue(
    'od_data', exchange, routing_key='od_data')

class OriginDestinationProducer(Producer):

    def send(self, message):

        self.publish(
            message,
            exchange=exchange,
            routing_key=od_data_queue.routing_key,
            declare=[od_data_queue],
        )

class OriginDestinationConsumer(ConsumerMixin):

    def __init__(self, connection, queue_name):
        self.connection = connection
        self.queue_name = queue_name
        self.client = get_client()
        self.db = self.client['mrt']
        self.collection = self.db['mrt_od_data']
        super().__init__()

    def get_consumers(self, Consumer, channel):
        return [Consumer(queues=[od_data_queue], callbacks=[self.on_message], prefetch_count=1)]

    def on_message(self, body, message):
        data = json.loads(message.body)
        self.process_data(data)
        message.ack()

    def process_data(self, data):
        file = data['filename']
        url_id = data['url_id']
        url = MRTResource.objects.get(id=url_id)
        print(f'Converting {file}...')
        st = time.time()
        data = convert_csv_to_json(f'{MRT_RAW_DATA_PATH}/{file}')
        print(f'Conversion time: {time.time() - st} seconds')
        print(f'Inserting {file} to MongoDB...')
        st = time.time()
        self.collection.insert_many(data)
        url.is_save_to_mongodb = True
        url.save()
        print(f'Insertion time: {time.time() - st} seconds')
        print(f'{file} inserted successfully.')