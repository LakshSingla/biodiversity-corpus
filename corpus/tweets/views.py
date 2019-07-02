from django.shortcuts import render
from django.http import JsonResponse
import tweepy
from tweepy import OAuthHandler
from .twitter_auth import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
from .analyse_tweets import get_location, get_tweet_sentiment

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

lat = 22
lon = 78
rad = 2000 # km

def tweets(request, keyword):
    # geolocator = Nominatim(user_agent="test")
    if request.method == 'GET':
        max_tweets = 10
        searched_tweets = [status._json for status in tweepy.Cursor(
            api.search, q=f"{keyword} -filter:retweets", lang='en', geocode=f'{lat},{lon},{rad}km').items(max_tweets)]
        resp = [{
            'text': tweet['text'],
            'location': get_location(tweet['text']),
            'sentiment': get_tweet_sentiment(tweet['text'])
        } for tweet in searched_tweets]
        return JsonResponse(resp)
