import tweepy
import json
import re
from tweepy import OAuthHandler
from witai import getchannel
# Authentication details. To  obtain these visit dev.twitter.com
consumer_key = 'W6w7r8IStfNsOvqaXo4mNkEIe'
consumer_secret = 'WLAuzE9F83y4Nm3vErP5PDE8mkmbDZCiivWL0RTadmwRasLsvt'
access_token = '3130630774-zLgwjt8dKjG0tDjm624IP9vFatlhWcq53iZ0cvW'
access_token_secret = 'UTQISn99sugTjcn3fszDJeIzLohdkYjaTANmKZMwzEddE'

# This is the listener, resposible for receiving data
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)

        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        #print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
        tweet = decoded['text'].encode('ascii', 'ignore')
        print tweet
        print getchannel(tweet)

    def on_error(self, status):
        print status

    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'


l = StdOutListener()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = tweepy.Stream(auth, l)

