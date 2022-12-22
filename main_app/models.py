from django.db import models

class Taz(models.Model):
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    age = models.IntegerField()
    note = models.TextField(max_length=250)
    image = models.ImageField()


