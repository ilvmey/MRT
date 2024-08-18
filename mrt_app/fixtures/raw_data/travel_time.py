import json


# TODO: 資料來源有誤，等待更正

def read_travel_time_info():
    filename = 'mrt_app/fixtures/raw_data/travel_time.json'
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
        travel_times = row['TravelTimes']
        for travel_time in travel_times:
            from_station = station_info_dict[travel_time['FromStationID']]
            to_station = station_info_dict[travel_time['ToStationID']]
            run_time = travel_time['RunTime']
            stop_time = travel_time['StopTime']

            data = {
                'model': 'mrt_app.traveltime',
                'pk': pk,
                'fields': {
                    'from_station': from_station,
                    'to_station': to_station,
                    'run_time': run_time,
                    'stop_time': stop_time,
                }
            }
            pk += 1

            output.append(data)

    with open('mrt_app/fixtures/travel_time.json', mode='w', encoding='utf-8') as file:
        json.dump(output, file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    rows = read_travel_time_info()
    convert_to_json(rows)
