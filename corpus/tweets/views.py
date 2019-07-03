from django.shortcuts import render
from django.http import JsonResponse
import tweepy
from tweepy import OAuthHandler
from .twitter_auth import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
from .analyse_tweets import get_location, get_tweet_sentiment, clean_tweet

from functools import reduce

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

lat = 22
lon = 78
rad = 2000  # km


def tweets(request, keyword):
    # geolocator = Nominatim(user_agent="test")
    if request.method == 'GET':
        max_tweets = 1000
        searched_tweets = [status._json for status in tweepy.Cursor(
            api.search, q=f"{keyword} -filter:retweets", lang='en').items(max_tweets)]
            # api.search, q=f"{keyword} -filter:retweets", lang='en', geocode=f'{lat},{lon},{rad}km').items(max_tweets)]
        
        pos, neg, neut = 0, 0, 0

        for tweet in searched_tweets:
            # print(tweet['created_at'])
            sentiment = get_tweet_sentiment(tweet['text'])
            get_location(tweet['text'])
            if sentiment == 'positive': pos += 1
            elif sentiment == 'negative': neg += 1
            elif sentiment == 'neutral': neut += 1

        resp = {
            'tweets': [
                {
                    'text': clean_tweet(tweet['text']),
                    # 'location': get_location(tweet['text']),
                    'sentiment': get_tweet_sentiment(tweet['text'])
                } for tweet in searched_tweets],
            
            'analysis': {
                'sentiment': {
                    'positive': pos,
                    'negative': neg,
                    'neutral': neut
                },
                'timeseries': None,
                'location': None
            }
        }

        return JsonResponse(resp)
