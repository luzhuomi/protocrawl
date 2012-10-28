from django.db import models

# Create your models here.

class Tweet(models.Model):
    age_band = models.CharField(max_length=10)
    gender   = models.CharField(max_length=10)
    race     = models.CharField(max_length=10)
    tweet    = models.CharField(max_length=200)
    mood     = models.CharField(max_length=20)
    location = models.CharField(max_length=10)
    latitude  = models.FloatField()
    longitude = models.FloatField()

def import_from_xls(fname):
    file = open(fname, 'r')
    for ln in file:
        cols = ln.strip("\r\n").split('\t')
        t = Tweet(age_band = cols[0],
                  gender   = cols[1],
                  race     = cols[2],
                  tweet    = cols[3],
                  mood     = cols[4],
                  location = cols[5],
                  latitude = cols[6],
                  longitude = cols[7]
                  )
        t.save()
    file.close()
        
