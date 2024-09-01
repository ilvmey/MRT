import csv
from io import StringIO
import time

import orjson
import pandas as pd
from multiprocessing import Pool, cpu_count

def convert_to_csv(raw_data):
    csv_file = StringIO(raw_data)
    reader = csv.reader(csv_file)

    return [row for row in reader]


def convert_to_objects(header, data_chunk):
    return [{header[i]: item[i] for i in range(len(header))} for item in data_chunk]

def convert_csv_to_json(csv_filename):
    df = pd.read_csv(csv_filename)
    df['日期'] = pd.to_datetime(df['日期'], format='%Y-%m-%d')
    return df.to_dict(orient='records')

    # print(f'Loading {csv_filename}...')

    # data = read_csv(csv_filename)
    # header = data.pop(0)

    # # Determine the number of chunks
    # num_chunks = cpu_count()
    # chunk_size = len(data) // num_chunks
    # data_chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    # # Use multiprocessing to convert data to objects
    # with Pool(num_chunks) as pool:
    #     results = pool.starmap(convert_to_objects, [(header, chunk) for chunk in data_chunks])

    # # Flatten the list of lists
    # objects = [obj for sublist in results for obj in sublist]
    # return objects

def read_csv(filename):

    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = [row for row in reader]
    return rows

def write_csv(filename, csv_data):
    with open(filename, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(csv_data)