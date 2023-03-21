from django.db import models


class PlantInformation(models.Model):
    moisture = models.FloatField(default=0.0)
    humidity = models.FloatField(default=0.0)
    temperature = models.FloatField(default=0.0)
    dateTime = models.DateTimeField(auto_now_add=True)
