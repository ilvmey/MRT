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


if __name__ == '__main__':
    rows = read_adjacency_station_info()
    convert_to_json(rows)
