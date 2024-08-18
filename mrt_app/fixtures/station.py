import csv
import json

filename = 'mrt_app/fixtures/station.csv'

with open(filename, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    rows = [row for row in reader]

output = []
for pk, row in enumerate(rows):
    data = {
        'model': 'mrt_app.station',
        'pk': pk,
        'fields': {
            'code': row[0],
            'name': row[1],
            'english_name': row[2]
        }
    }

    output.append(data)

with open('mrt_app/fixtures/station.json', mode='w', encoding='utf-8') as file:
    json.dump(output, file, ensure_ascii=False, indent=4)
