import requests
import csv
from io import StringIO

def get_mrt_url():
    TAIPEI_MRT_DATA_LIST_URL = 'https://data.taipei/api/dataset/63f31c7e-7fc3-418b-bd82-b95158755b4d/resource/eb481f58-1238-4cff-8caa-fa7bb20cb4f4/download'

    response = requests.get(TAIPEI_MRT_DATA_LIST_URL)

    if response.status_code == 200:
        result = convert_to_csv(response.text)
        result = [r[-1] for r in result]
        return result[1:]
    else:
        print(f"error: {response.status_code}")

def download(urls):
    for url in urls:
        response = requests.get(url)
        result = convert_to_csv(response.text)
        result

def convert_to_csv(raw_data):
    csv_file = StringIO(raw_data)
    reader = csv.reader(csv_file)

    return [row for row in reader]

if __name__ == '__main__':
    urls = get_mrt_url()
    download(urls)
