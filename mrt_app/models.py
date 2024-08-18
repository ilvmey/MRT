from django.db import models

class Station(models.Model):
    code = models.CharField(max_length=4)
    name = models.CharField(max_length=25)
    english_name = models.CharField(max_length=50)