import time

import requests
from misc.data_path import MRT_RAW_DATA_PATH
from utils.data_processor import convert_to_csv, write_csv

from django.core.management.base import BaseCommand
import os
import django

django.setup()

from mrt_app.models import MRTResource


def download(url):
    filename = url.filename
    print(f'Downloading {filename}...')
    st = time.time()
    response = requests.get(url.url)
    print(f'Downloaded in {time.time() - st:.2f} seconds.')
    csv_data = convert_to_csv(response.text)
    print(f'Writing to {filename}...')
    write_csv(f'{MRT_RAW_DATA_PATH}/{filename}', csv_data)
    url.is_download = True
    url.save()
    print('done!')


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        urls = MRTResource.objects.filter(is_download=False).order_by('id')
        for url in urls:
            download(url)