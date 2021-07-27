from django.db import models

class Points(models.Model):
    point = models.CharField(max_length=1000)
    closestPoint = models.FloatField()
