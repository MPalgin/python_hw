from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()


class Measurement(models.Model):
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, default=None, related_name='measurements')
    picture = models.ImageField(default=None, null=True)
