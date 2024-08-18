import django
import os

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mrt.settings')

# Setup Django
django.setup()
# Import models after Django setup
from mrt_app.models import AdjacencyStation, Station
# Query objects
stations = Station.objects.all()
print(len(stations))

station = Station.objects.get(code='R07')
origin_stations = station.origin_stations.all()

for origin_station in origin_stations:
    print(origin_station.destination_station.code)