import json

# https://tdx.transportdata.tw/api-service/swagger/basic/268fc230-2e04-471b-a728-a726167c1cfc#/Metro/MetroApi_Station_2092

filename = 'mrt_app/fixtures/raw_data/station.json'

with open(filename, mode='r', encoding='utf-8') as file:
    with open(filename, mode='r', encoding='utf-8') as file:
        rows = json.load(file)

output = []
for pk, row in enumerate(rows):
    data = {
        'model': 'mrt_app.station',
        'pk': pk,
        'fields': {
            'code': row['StationID'],
            'name': row['StationName']['Zh_tw'],
            'english_name': row['StationName']['En'],
        }
    }

    output.append(data)

with open('mrt_app/fixtures/station.json', mode='w', encoding='utf-8') as file:
    json.dump(output, file, ensure_ascii=False, indent=4)
