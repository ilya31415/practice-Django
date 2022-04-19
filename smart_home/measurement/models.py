from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True)


class Measurement(models.Model):
    sensor = models.OneToOneField(Sensor, on_delete=models.CASCADE, primary_key=True, related_name='Sensor')
    temperature = models.IntegerField()
    data_measurement = models.DateField(auto_now=True)
