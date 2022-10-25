from django.db import models
import datetime
# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()

class Song(models.Model):
    Artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    date_released = models.DateField(default = datetime.date.today)
    likes =  models.IntegerField()
    artist_id =  models.IntegerField()

class Lyrics(models.Model):
    content = models.ForeignKey(Song, on_delete=models.CASCADE)
    song_id =  models.IntegerField()