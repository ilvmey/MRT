import orjson
import time
from django.core.management.base import BaseCommand
from multiprocessing import Pool, cpu_count
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mrt.settings')  # Replace with your settings module
django.setup()

from mrt_app.models import OriginDestination
from mrt_app.fixtures.raw_data.od import get_json_files

def convert_to_objects(data_chunk):
    """Convert a chunk of data to OriginDestination objects."""
    return [OriginDestination(**item['fields']) for item in data_chunk]

def process_file(path, file):
    """Process a single JSON file."""
    print(f'Loading {file}...')
    st = time.time()

    with open(f'{path}/{file}', 'rb') as f:
        data = orjson.loads(f.read())
    print(f'Loaded {file} in {time.time() - st:.2f} seconds')

    st = time.time()
    print(f'Converting {file} to objects...')

    # Determine the number of chunks
    num_chunks = cpu_count()
    chunk_size = len(data) // num_chunks
    data_chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    # Use multiprocessing to convert data to objects
    with Pool(num_chunks) as pool:
        results = pool.map(convert_to_objects, data_chunks)

    # Flatten the list of lists
    objects = [obj for sublist in results for obj in sublist]
    print(f'Converted {file} to objects in {time.time() - st:.2f} seconds')

    st = time.time()
    print(f'Saving {file} to database...')
    OriginDestination.objects.bulk_create(objects, batch_size=10000)  # Adjust batch size as needed
    print(f'Saved {file} to database in {time.time() - st:.2f} seconds')

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        path = 'mrt_app/fixtures/mrt'
        files = get_json_files()

        for file in files:
            process_file(path, file)
