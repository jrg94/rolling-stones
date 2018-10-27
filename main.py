import tweepy

auth = tweepy.OAuthHandler("oDGPSLRthhVvbrk22aF5vgldV", "IigqG87FbIuhcZpHUxuq4O2adgrFuX3eg8dwqRNulffNrzYifP")
auth.set_access_token("355356323-rPDfRC56bekq7aHlYh0iXYcxxjqPiiJuD2ngr2Fa", "5LiGqpUtkiZKrbOpOdJvekxfgssDaqqtVHfa2c3qpjrAZ")

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text
