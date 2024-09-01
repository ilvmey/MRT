from django.core.management.base import BaseCommand
import os
import django
import requests
from utils.data_processor import convert_to_csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mrt.settings')  # Replace with your settings module
django.setup()

from mrt_app.models import MRTResource


def get_resource():
    TAIPEI_MRT_DATA_LIST_URL = 'https://data.taipei/api/dataset/63f31c7e-7fc3-418b-bd82-b95158755b4d/resource/eb481f58-1238-4cff-8caa-fa7bb20cb4f4/download'

    response = requests.get(TAIPEI_MRT_DATA_LIST_URL)

    if response.status_code == 200:
        result = convert_to_csv(response.text)
        result = [r[-1] for r in result]
        result.pop(0)  # remove header
        return result
    else:
        raise Exception(f"error: {response.status_code}")

def convert_to_objects(urls):
    for url in urls:
        MRTResource.objects.get_or_create(url=url)

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        urls = get_resource()
        convert_to_objects(urls)
