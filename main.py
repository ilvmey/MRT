import csv
import json
import requests
import time
from io import StringIO


def get_mrt_url():
    TAIPEI_MRT_DATA_LIST_URL = 'https://data.taipei/api/dataset/63f31c7e-7fc3-418b-bd82-b95158755b4d/resource/eb481f58-1238-4cff-8caa-fa7bb20cb4f4/download'

    response = requests.get(TAIPEI_MRT_DATA_LIST_URL)

    if response.status_code == 200:
        result = convert_to_csv(response.text)
        result = [r[-1] for r in result]
        result.pop(0)  # remove header
        return result
    else:
        print(f"error: {response.status_code}")


def download(url):
    filename = get_csv_name_from_url(url)
    print(f'Downloading {filename}...')
    response = requests.get(url)
    csv_data = convert_to_csv(response.text)
    print(f'Writing to {filename}...')
    write_csv(filename, csv_data)
    print('done!')


def convert_to_csv(raw_data):
    csv_file = StringIO(raw_data)
    reader = csv.reader(csv_file)

    return [row for row in reader]


def convert_to_json(data):
    info = read_station_info()
    data


def read_csv():
    filename = '201701.csv'

    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = [row for row in reader]
    return rows
def write_csv(filename, csv_data):
    with open(filename, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(csv_data)

def read_station_info():
    filename = 'mrt_app/fixtures/station.json'
    with open(filename, mode='r', encoding='utf-8') as file:
        data = json.load(file)

    return data

def get_csv_name_from_url(url):
    return url.split('_')[-1]

if __name__ == '__main__':
    urls = get_mrt_url()
    for url in urls:
        download(url)
    # data = read_csv()
    # data.pop(0)
    # convert_to_json(data)
