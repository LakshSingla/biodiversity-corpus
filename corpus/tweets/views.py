from django.shortcuts import render
from django.http import JsonResponse
import tweepy
from tweepy import OAuthHandler
from .twitter_auth import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


def tweets(request, keyword):
    if request.method == 'GET':
        max_tweets = 50
        searched_tweets = [status._json for status in tweepy.Cursor(
            api.search, q=keyword).items(max_tweets)]
        return JsonResponse({
            "tweets": searched_tweets
        })
