from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=100)
    director = models.CharField(max_length=50)
    arc = models.CharField(max_length=100, default='')
    release_date = models.DateField()
    rating = models.IntegerField()
    summary = models.CharField(max_length=10000)