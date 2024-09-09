from ninja import NinjaAPI, Schema
from typing import List
from django.shortcuts import get_object_or_404

from mrt_app.models import Station

api = NinjaAPI()

class DestinationSchema(Schema):
    id: int
    code: str
    name: str

    class Config:
        orm_mode = True

class StationSchema(Schema):
    id: int
    code: str
    name: str
    english_name: str
    destinations: List[DestinationSchema]



@api.get("/stations/", response=List[StationSchema])
def get_stations(request):
    stations = Station.objects.prefetch_related('destinations').all()
    return stations


@api.get("/stations/{station_id}/", response=StationSchema)
def get_station(request, station_id: int):
    station = get_object_or_404(Station.objects.prefetch_related('destinations'), id=station_id)
    return station

