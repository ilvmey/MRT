import django
import os

from dijkstar import Graph, find_path

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mrt.settings')

# Setup Django
django.setup()

from mrt_app.models import Station


class MRT:
    def __init__(self):
        self.graph = Graph()
        self.stations = Station.objects.all()

        for station in self.stations:
            for destination in station.destinations.all():
                self.graph.add_edge(station.code, destination.code, edge=1)

        for origin in self.stations:
            for destination in self.stations:
                # find_path(graph, 'R14', 'BL16')
                path = find_path(self.graph, origin.code, destination.code)
                print(path.nodes, len(path.nodes))

    def get_shortest_path(self, origin, destination):
        return find_path(self.graph, origin.code, destination.code)