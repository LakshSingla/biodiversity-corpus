import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
# import MySQLdb
import csv
import random
import pprint
from analyse_tweets import get_tweet_sentiment

consumer_key = "vPMhh55Wf2mGyUWoQZrOP1YWu"
consumer_secret = "Dooskx16LcJek2UqnaCLFQzJdgJSNTmf5Bv4sn8zFgXz2Htzmr"

access_token = "886549911587532800-CVZKNSyVc3AiKq4PSzDYccfG5x1yLE6"
access_token_secret = "yrCSB4oAu829ZS87UPAOQHjkcTrES6tzXe8TImq8FH974"

pp = pprint.PrettyPrinter(indent=2)

# Create your MySQL schema and connect to database, ex: mysql> SET PASSWORD FOR 'root'@'localhost' = PASSWORD('newpwd');
# db=MySQLdb.connect(host='localhost', user='root', passwd='newpwd', db='twitter')
# db.set_character_set('utf8')

# Coords = dict()
# XY = []
# curr=db.cursor()

# per request, write output to csv, rather than mysql. Be aware of limited rows to csv. The streaming API will return millions of rows per day.
#csvfile = open('geopy_results.csv','wb')
#csvwriter = csv.writer(csvfile)
#csvwriter.writerow(['UserID', 'Date', 'Lat', 'Long', 'Text'])


class StdOutListener(StreamListener):
    def on_status(self, status):
        # print("Tweet Text: ", status.text)
        # print("Time Stamp: ", status.created_at)
        print("*" * 50)
        # print(status)
        pp.pprint(status)
        print("*" * 50)


    # """ A listener handles tweets that are the received from the stream.
    # This is a basic listener that inserts tweets into MySQLdb.
    # """
    # def on_status(self, status):
    # print "Tweet Text: ",status.text
    # text = status.text
    # print "Time Stamp: ",status.created_at
    # try:
    # Coords.update(status.coordinates)
    # XY = (Coords.get('coordinates'))  #Place the coordinates values into a list 'XY'
    # print "X: ", XY[0]
    # print "Y: ", XY[1]
    # except:
    # Often times users opt into 'place' which is neighborhood size polygon
    # Calculate center of polygon
    # Box = status.place.bounding_box.coordinates[0]
    # XY = [(Box[0][0] + Box[2][0])/2, (Box[0][1] + Box[2][1])/2]
    # print "X: ", XY[0]
    # print "Y: ", XY[1]
    # Comment out next 4 lines to avoid MySQLdb to simply read stream at console
    # curr.execute("""INSERT INTO TwitterFeed2 (UserID, Date, Lat, Lng, Text) VALUES
    # (%s, %s, %s, %s, %s);""",
    # (status.id_str,status.created_at,XY[1],XY[0],text))
    # db.commit()

    # Alternatively write to CSV. CSV's. limited
    # csvwriter.writerow([unicode(status.id_str).encode("utf-8"),unicode(status.created_at).encode("utf-8"),XY[1],XY[0],unicode(status.text).encode("utf-8")])


def main():
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    # stream = Stream(auth, l, timeout=30.0)
    api = tweepy.API(auth)
    query='forest fire'
    max_tweets = 20
    searched_tweets = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]
    for tweet in searched_tweets:
        print(tweet.text)
        print(get_tweet_sentiment(tweet.text))
    print(len(searched_tweets))
    # Only records 'locations' OR 'tracks', NOT 'tracks (keywords) with locations'
    # while True:
        # try:
            # Call tweepy's userstream method
            # Use either locations or track, not both
            # These coordinates are approximate bounding box around USA
            # stream.filter(locations=[-125, 25, -65, 48])
            # stream.filter(track=['jammu'])## This will feed the stream all mentions of 'keyword'
            # break
        # except Exception:
            # Abnormal exit: Reconnect
            # nsecs = random.randint(60, 63)
            # time.sleep(nsecs)


if __name__ == '__main__':
    main()
