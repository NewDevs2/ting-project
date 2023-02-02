from django.db import models

# Create your models here.

class AptData(models.Model):
    month         = models.IntegerField()
    year            = models.IntegerField()
    price_apt   = models.IntegerField()
    city              = models.TextField()

class SotckData(models.Model):
    month         = models.IntegerField()
    year            = models.IntegerField()
    price_stock   = models.IntegerField()
    index_name  = models.TextField()
