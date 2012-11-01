from django.db import models
import dateutil.parser as p

# Create your models here.

class Tweet(models.Model):
    time_posted = models.DateTimeField()
    age_band = models.CharField(max_length=10)
    gender   = models.CharField(max_length=10)
    race     = models.CharField(max_length=10)
    tweet    = models.CharField(max_length=200)
    mood     = models.CharField(max_length=20)
    location = models.CharField(max_length=10)
    latitude  = models.FloatField()
    longitude = models.FloatField()
    day_type = models.CharField(max_length=10)

def import_from_xls(fname):
    file = open(fname, 'r')
    for ln in file:
        cols = ln.strip("\r\n").split('\t')
        if len(cols[5])>0:
            t = Tweet(time_posted = p.parse(cols[0]),
                      age_band = cols[1] if len(cols[1]) >0 else 'UNKNOWN',
                      gender   = cols[2] if len(cols[2]) >0 else 'UNKNOWN',
                      race     = cols[3] if len(cols[3]) >0 else 'UNKNOWN',
                      tweet    = cols[4],
                      mood     = cols[5] if len(cols[5]) >0 else 'UNKNOWN',
                      location = cols[6] if len(cols[6]) >0 else 'UNKNOWN',
                      latitude = cols[7],
                      longitude = cols[8],
                      day_type  = cols[9],
                )
            t.save()
    file.close()
        
'''
update main_tweet set location = 'Universal Studio' where location = 'USS';
update main_tweet set location = 'Hard Rock Hotel' where location = 'hard rock hotel';
update main_tweet set location = 'Siloso Beach' where location = 'Siloso';
update main_tweet set location = 'Resort World Singapore' where location = 'RWS';
'''
