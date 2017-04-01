import tweepy
import json
import re
from tweepy import OAuthHandler
from witai import getchannel
import pprint
from flock import send_tweet
# from flock import send_tweet
# Authentication details. To  obtain these visit dev.twitter.com
consumer_key = 'M39Nk7BorqtWj3jyHAhRnSNyd'
consumer_secret = 'Jjzw2WeWN8oDuevqhSMCYD629MVxMCBRhfo3mit08IHkMNEYIE'
access_token = '3130630774-mpgMGAyLTfQweuXqTw9Q9UHNQv5tHEbunXB6bnV'
access_token_secret = '0EhhSbA4DTGIz2zdT1N4zPAXgAPw7txYRWxzByP8A771o'


class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        decoded = json.loads(data)
        print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
        tweet = decoded['text'].encode('ascii', 'ignore')
        # print decoded
        channel = getchannel(decoded['text'].encode('ascii', 'ignore'))
        send_tweet(decoded)

    def on_error(self, status):
        print status

    # def get_tweet_sentiment(self, tweet):
    #     analysis = TextBlob(self.clean_tweet(tweet))
    #     # set sentiment
    #     if analysis.sentiment.polarity > 0:
    #         return 'positive'
    #     elif analysis.sentiment.polarity == 0:
    #         return 'neutral'
    #     else:
    #         return 'negative'


l = StdOutListener()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = tweepy.Stream(auth, l)

