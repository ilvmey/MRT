import django
import os

from dijkstar import Graph, find_path

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mrt.settings')

# Setup Django
django.setup()

from mrt_app.models import Station


graph = Graph()
stations = Station.objects.all()

for station in stations:
    for destination in station.destinations.all():
        graph.add_edge(station.code, destination.code, edge=1)

find_path(graph, 'R14', 'BL16')

