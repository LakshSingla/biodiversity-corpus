from djongo import models

class TweetSearch(models.Model):
    tweet = models.CharField(max_length=300)
    date = models.CharField(max_length=200)
    sentiment = models.CharField(max_length=30)
    latitude = models.IntegerField()
    longitude = models.IntegerField()
