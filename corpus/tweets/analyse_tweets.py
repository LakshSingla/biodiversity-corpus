import re
from textblob import TextBlob
from geopy.geocoders import Nominatim, GoogleV3
from geopy.exc import GeocoderTimedOut
from geopy.point import Point
import spacy

INDIAN_BOUNDS = [Point(latitude=35.4940095078, longitude=68.1766451354), Point(latitude=7.96553477623, longitude=97.4025614766)]

def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


def get_tweet_sentiment(tweet):
    ''' 
    Utility function to classify sentiment of passed tweet 
    using textblob's sentiment method 
    '''
    # create TextBlob object of passed tweet text
    analysis = TextBlob(clean_tweet(tweet))
    # set sentiment
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'

    return 'negative'


def get_location(tweet):
    cleaned_tweet = clean_tweet(tweet)
    geolocator = Nominatim(user_agent="test")
    # google_geolocator = GoogleV3(api_key='AIzaSyDUrM4reXIG5A8GoZEPrKnPuGYIV0Do7dk')
    sp = spacy.load('en_core_web_sm') 
    sen = sp(cleaned_tweet)
    location = None
    for entity in sen.ents:
        # print(entity.text + ' - ' + entity.label_ + ' - ' + str(spacy.explain(entity.label_))) 
        if entity.label_ == 'LOC':
            print(f"LOCATION FOUND - {entity.text}")
            try:
                location = geolocator.geocode(entity.text)
            except Exception:
                pass
            if location is not None:
                # pass
                print(tweet)
                print(f"{entity.text} - {location.latitude}, {location.longitude}")
    return location
