from django.db import models

# Create your models here.

class Film(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(default=None)
    relaseDate = models.IntegerField(default=1900)
    poster = models.ImageField(upload_to='posters', default=None)