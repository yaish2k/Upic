from django.db import models

class Place(models.Model):

    place_id = models.CharField(max_length=200)
    adress = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    lat = models.FloatField(default=0)
    long = models.FloatField(default=0)

    def __unicode__(self):
        return self.name

class Tweets(models.Model):
    user_id = models.IntegerField(default=0)
    post_id = models.IntegerField(default=0)
    text = models.CharField(max_length=200)
    user_image = models.URLField(default="")
    tweet_image = models.URLField(default="")
    time_stamp = models.DateTimeField()
    place = models.ForeignKey(Place)
    country = models.CharField(max_length=50)
    likes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.text




