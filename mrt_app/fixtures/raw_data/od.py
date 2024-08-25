import csv
import orjson
import os
import time

path = 'mrt_app/fixtures/raw_data/mrt'

def get_csv_files():
    csv_files = [f for f in os.listdir(path) if f.endswith('.csv')]
    return csv_files

def read_csv(filename):
    rows = []
    st = time.time()
    with open(f'{path}/{filename}', mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = [r for r in reader]

    rows.pop(0)
    print(f'Read {filename} in {time.time() - st:.2f} seconds.')
    return rows

def write_json(rows, filename, pk=1):
    path = 'mrt_app/fixtures'
    output = []
    st = time.time()
    for row in rows:
        data = {
           'model':'mrt_app.origindestination',
            'pk': pk,
            'fields': {
                'date': row[0],
                'hour': int(row[1]),
                'origin_station': row[2],
                'destination_station': row[3],
                'count': int(row[4])
            }
        }
        output.append(data)
        pk += 1
    print(f'Process {filename} in {time.time() - st:.2f} seconds.')

    st = time.time()
    with open(f'{path}/{filename}', mode='wb') as file:
        file.write(orjson.dumps(output))
    print(f'Write {filename} in {time.time() - st:.2f} seconds.')

def read_json(filename):
    path = 'mrt_app/fixtures'
    with open(f'{path}/{filename}', mode='rb') as file:
        data = orjson.loads(file.read())
    return data

def generate_json_files_from_csv():
    csv_files = get_csv_files()
    pk = 1
    for csv_file in csv_files:
        rows = read_csv(csv_file)
        json_filename = csv_file.replace('.csv', '.json')
        write_json(rows, json_filename, pk)
        pk += len(rows)

def get_json_files():
    csv_files = get_csv_files()
    filenames = [f.replace('.csv', '.json') for f in csv_files]
    return filenames

def check_json_files_pk():
    filenames = get_json_files()
    next_pk = 1
    for filename in filenames:
        print(f'Checking {filename}...')
        data = read_json(filename)
        last_pk = data[-1]['pk']
        if data[0]['pk'] != next_pk:
            print(f'Error: {filename} has invalid PK.')
        next_pk = last_pk +1
if __name__ == '__main__':
    # generate_json_files_from_csv()
    check_json_files_pk()