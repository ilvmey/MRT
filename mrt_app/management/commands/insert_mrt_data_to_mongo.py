import os
import time
from django.core.management.base import BaseCommand

import django
import pymongo

from message_queue.base import conn, od_data_queue, OriginDestinationProducer
from misc.data_path import MRT_RAW_DATA_PATH

from utils.data_processor import convert_csv_to_json
from utils.mongodb_client import get_client

django.setup()

from mrt_app.models import MRTResource

def get_raw_data_filenames():
    return [f for f in os.listdir(MRT_RAW_DATA_PATH) if os.path.isfile(os.path.join(MRT_RAW_DATA_PATH, f))]


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        client = get_client()
        db = client['mrt']
        collection = db['mrt_od_data']
        collection.create_index([('日期', pymongo.ASCENDING), ('時段', pymongo.ASCENDING)])
        collection.create_index([('進站', pymongo.ASCENDING), ('日期', pymongo.ASCENDING)])
        files = get_raw_data_filenames()
        urls = MRTResource.objects.filter(is_save_to_mongodb=False)

        for file in files:
            url = next(filter(lambda url: url.filename == file, urls), None)
            if url is None:
                continue
            OriginDestinationProducer
            producer = OriginDestinationProducer(conn, od_data_queue)
            producer.send({'filename': file, 'url_id': url.id})
