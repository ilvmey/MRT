from django.db import models


class Station(models.Model):
    code = models.CharField(max_length=4)
    name = models.CharField(max_length=25)
    english_name = models.CharField(max_length=50)


# class OriginDestination(models.Model):
#     date = models.DateField()
#     hour = models.IntegerField()
#     origin_station = models.ForeignKey(
#         Station, on_delete=models.CASCADE, related_name='origin_stations')
#     destination_station = models.ForeignKey(
#         Station, on_delete=models.CASCADE, related_name='destination_stations')
#     count = models.IntegerField(default=0)


class TravelTime(models.Model):
    from_station = models.ForeignKey(
        Station, on_delete=models.CASCADE, related_name='from_station')
    to_station = models.ForeignKey(
        Station, on_delete=models.CASCADE, related_name='to_station')
    run_time = models.IntegerField()
    stop_time = models.IntegerField()


class AdjacencyStation(models.Model):
    origin_station = models.ForeignKey(
        Station, on_delete=models.CASCADE, related_name='origin_stations')
    destination_station = models.ForeignKey(
        Station, on_delete=models.CASCADE, related_name='destination_stations')
    distance = models.IntegerField(default=1)
