import django
import os

from dijkstar import Graph, find_path

from utils.mongodb_client import get_client

# Setup Django
django.setup()

from mrt_app.models import Station


class MRT:
    def __init__(self):
        self.graph = Graph()
        self.stations = Station.objects.all()
        self.client = get_client()

        for station in self.stations:
            for destination in station.destinations.all():
                self.graph.add_edge(station.code, destination.code, edge=1)

    def get_shortest_path(self, origin, destination):
        return find_path(self.graph, origin.code, destination.code)

    def get_station(self, code):
        return next(filter(lambda station: station.code == code, self.stations), None)


if __name__ == '__main__':
    mrt = MRT()
    origin = mrt.get_station(code='R14')
    destination = mrt.get_station(code='BL16')
    path = mrt.get_shortest_path(origin, destination)
    print(path.nodes, len(path.nodes))