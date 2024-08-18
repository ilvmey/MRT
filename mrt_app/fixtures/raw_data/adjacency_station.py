import json


def read_adjacency_station_info():
    filename = 'mrt_app/fixtures/raw_data/adjacency_station.json'
    with open(filename, mode='r', encoding='utf-8') as file:
        data = json.load(file)

    return data


def read_station_info():
    filename = 'mrt_app/fixtures/station.json'
    with open(filename, mode='r', encoding='utf-8') as file:
        data = json.load(file)

    return data


def convert_to_json(rows):
    station_info = read_station_info()
    station_info_dict = {}
    for station in station_info:
        station_info_dict[station['fields']['code']] = station['pk']

    output = []
    pk = 1
    for row in rows:
        from_station_id = station_info_dict[row['from']]
        for to_station in row['to']:
            to_station_id = station_info_dict[to_station]
            data = {
                'model': 'mrt_app.adjacencystation',
                'pk': pk,
                'fields': {
                    'origin_station': from_station_id,
                    'destination_station': to_station_id,
                }
            }
            pk += 1
            output.append(data)
    with open('mrt_app/fixtures/adjacency_station.json', mode='w', encoding='utf-8') as file:
        json.dump(output, file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    rows = read_adjacency_station_info()
    convert_to_json(rows)
