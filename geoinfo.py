import tweepy
import re
from tweepy import OAuthHandler
from textblob import TextBlob
import json

class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''
    def __init__(self):

        try:
            self.auth = tweepy.OAuthHandler("oDGPSLRthhVvbrk22aF5vgldV", "IigqG87FbIuhcZpHUxuq4O2adgrFuX3eg8dwqRNulffNrzYifP")
            self.auth.set_access_token("355356323-rPDfRC56bekq7aHlYh0iXYcxxjqPiiJuD2ngr2Fa", "5LiGqpUtkiZKrbOpOdJvekxfgssDaqqtVHfa2c3qpjrAZ")
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        analysis = TextBlob(self.clean_tweet(tweet))
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, query, counts):
        tweets = []
        try:
            max_tweets = counts
            fetched_tweets = [status for status in tweepy.Cursor(self.api.search, q=query).items(max_tweets)]
            i = 0
            for tweet in fetched_tweets:
                if tweet.user.geo_enabled:
                    parsed_tweet = {}
                    parsed_tweet['text'] = tweet.text
                    parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)
                    parsed_tweet['coordinates'] = tweet.coordinates
                    parsed_tweet['created_at'] = tweet.created_at

                    tweets.append(parsed_tweet);

            print(json.dumps(tweets))

            return tweets

        except tweepy.TweepError as e:
            print(str(e))

def main():
    api = TwitterClient()
    tweets = api.get_tweets(query = 'Hurricane', counts = 100)
    if tweepy.TweepError:
        return tweepy.TweepError
    """print(tweets)"""



"""
    i = 0
    for tweet in tweets:
        i = i+1
        if i % 1 == 0:
            print(i,": ")
            print(tweet.text)
    print(len(tweets))
"""

if __name__ == "__main__":
    main()
