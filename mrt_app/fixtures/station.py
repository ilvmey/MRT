import json

# https://tdx.transportdata.tw/api-service/swagger/basic/268fc230-2e04-471b-a728-a726167c1cfc#/Metro/MetroApi_Station_2092


def load_json(filename):
    with open(filename, mode='r', encoding='utf-8') as file:
        rows = json.load(file)
    return rows
def read_station_raw_data():
    filename = 'mrt_app/fixtures/raw_data/station.json'
    return load_json(filename)

def read_station_info():
    filename = 'mrt_app/fixtures/station.json'
    return load_json(filename)



def generate_station_info(rows):
    output = []
    for pk, row in enumerate(rows):
        data = {
            'model': 'mrt_app.station',
            'pk': pk+1,
            'fields': {
                'code': row['StationID'],
                'name': row['StationName']['Zh_tw'],
                'english_name': row['StationName']['En'],
            }
        }

        output.append(data)

    with open('mrt_app/fixtures/station.json', mode='w', encoding='utf-8') as file:
        json.dump(output, file, ensure_ascii=False, indent=4)

def read_adjacency_station_raw_data():
    filename = 'mrt_app/fixtures/raw_data/adjacency_station.json'
    return load_json(filename)

def add_destinations(stations, adjacency_stations):
    station_dict = {}
    for station in stations:
        station_dict[station['fields']['code']] = station['pk']
    for adjacency_station in adjacency_stations:
        origin_station_id = station_dict[adjacency_station['from']]
        station = next(filter(lambda x: x['pk'] == origin_station_id, stations))
        station['fields']['destinations'] = []
        destination_stations = adjacency_station['to']
        for destination_station in destination_stations:
            destination_station_id = station_dict[destination_station]
            station['fields']['destinations'].append(destination_station_id)
    with open('mrt_app/fixtures/station.json', mode='w', encoding='utf-8') as file:
        json.dump(stations, file, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    # rows = read_station_raw_data() # 資料有缺漏, 勿用
    # generate_station_info(rows)
    stations = read_station_info()
    adjacency_stations = read_adjacency_station_raw_data()
    add_destinations(stations, adjacency_stations)
