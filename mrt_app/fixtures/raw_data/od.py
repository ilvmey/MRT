import csv
import json
import time

path = 'mrt_app/fixtures/raw_data'
def read_csv():
    filename = '201702.csv'
    rows = []
    st = time.time()
    with open(f'{path}/{filename}', mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            # if i > 10:
            #     break
            rows.append(row)
    rows.pop(0)
    print(f'Read {filename} in {time.time() - st:.2f} seconds.')
    return rows

def write_json(rows):
    path = 'mrt_app/fixtures'
    filename = '201702.json'
    output = []
    i = 7581601  # indexed for primary key in Django model.
    st = time.time()
    for row in rows:
        data = {
           'model':'mrt_app.origindestination',
            'pk': i,
            'fields': {
                'date': row[0],
                'hour': int(row[1]),
                'origin_station': row[2],
                'destination_station': row[3],
                'count': int(row[4])
            }
        }
        output.append(data)
        i += 1
    print(f'Process {filename} in {time.time() - st:.2f} seconds.')
    st = time.time()
    with open(f'{path}/{filename}', mode='w', encoding='utf-8') as file:
        json.dump(output, file, indent=4, ensure_ascii=False)
    print(f'Write {filename} in {time.time() - st:.2f} seconds.')

rows = read_csv()
write_json(rows)