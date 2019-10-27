from django.utils import timezone

from django.db import models


# Create your models here.
class Sensor(models.Model):
    name = models.CharField(max_length=50)
    last_value = models.TextField()


class SensorData(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    value = models.FloatField(default=0)
    timestamp = models.DateTimeField(default=timezone.now())
