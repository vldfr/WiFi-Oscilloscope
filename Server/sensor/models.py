from django.utils import timezone

from django.db import models


# Create your models here.
class Sensor(models.Model):
    name = models.CharField(max_length=50)
    last_value = models.TextField()


class SensorReadingGroup(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now())


class SensorData(models.Model):
    group = models.ForeignKey(SensorReadingGroup, on_delete=models.CASCADE, blank=True, null=True)
    value = models.FloatField(default=0)
    timestamp = models.DateTimeField(default=timezone.now())
