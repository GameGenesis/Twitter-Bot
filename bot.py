import tweepy #Twitter's API (Install tweepy into your project folder)
import time

#Your API keys (Sign up for a twitter developer account)
consumer_key = 'XXX'
consumer_secret = 'XXX'

#Your access tokens (Sign up for a twitter developer account)
key = 'XXX'
secret = 'XXX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)
#Write out a test tweet
api.update_status('Twitter Bot Test Tweet!')

#The hashtag you want to filter by
hashtag = "#indiedev"
#The number of tweets with the hashtag you want to grab
tweetnumber = 10

def searchBot():
    tweets = tweepy.Cursor(api.search, hashtag).items(tweetnumber) #Grab the first [tweetnumber] of tweets containing the hashtag
    for tweet in tweets:
        try:
            tweet.favorite() #Like the tweet
            tweet.retweet() #Retweet it
            api.create_friendship(tweet.user.id) #Follow the user
            print('Retweeted!')
            time.sleep(3)
        except tweepy.TweepError as e:
            print(e.reason) #Print the error
            time.sleep(3)

#Runs the method every 120 seconds
while True:
    searchBot()
    time.sleep(120)