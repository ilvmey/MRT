from django.db import models


class MRTResource(models.Model):
    url = models.URLField(max_length=300, unique=True)
    is_download = models.BooleanField(default=False)
    is_save_to_mongodb = models.BooleanField(default=False)

    @property
    def filename(self):
        return self.url.split('_')[-1]

class Station(models.Model):
    code = models.CharField(max_length=4)
    name = models.CharField(max_length=25)
    english_name = models.CharField(max_length=50)
    destinations = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='origin_stations')

    def __str__(self):
        return f"{self.name} ({self.code})"


class OriginDestination(models.Model):
    date = models.DateField()
    hour = models.IntegerField()
    origin_station = models.CharField(max_length=30)
    destination_station = models.CharField(max_length=30)
    count = models.IntegerField(default=0)


class TravelTime(models.Model):
    from_station = models.ForeignKey(
        Station, on_delete=models.CASCADE, related_name='from_station')
    to_station = models.ForeignKey(
        Station, on_delete=models.CASCADE, related_name='to_station')
    run_time = models.IntegerField()
    stop_time = models.IntegerField()
