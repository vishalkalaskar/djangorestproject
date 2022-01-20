from django.db import models


class Studentmodel(models.Model):
    name = models.CharField(max_length=30)
    roll = models.IntegerField()
    city = models.CharField(max_length=30)