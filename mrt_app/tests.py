import django
import os

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mrt.settings')

# Setup Django
django.setup()
# Import models after Django setup
from mrt_app.models import Station
# Query objects
stations = Station.objects.all()
print(len(stations))

station = Station.objects.get(code='R07')

for destination in station.destinations.all():
    print(destination.code)