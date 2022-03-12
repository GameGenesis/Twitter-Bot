import tweepy
import time

#Your API key and secret (Sign up for a twitter developer account)
CONSUMER_KEY = 'XXX'
CONSUMER_SECRET = 'XXX'

#Your access tokens (Sign up for a twitter developer account)
ACCESS_TOKEN_KEY = 'XXX'
ACCESS_TOKEN_SECRET = 'XXX'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
#Write out a test tweet
api.update_status('Twitter Bot Test Tweet!')

#The hashtag you want to filter by
HASHTAG = "#indiedev"
#The number of tweets with the hashtag you want to grab
NUMBER_OF_TWEETS = 10

def searchBot():
    tweets = tweepy.Cursor(api.search, HASHTAG).items(NUMBER_OF_TWEETS) #Grab the first [tweetnumber] of tweets containing the hashtag
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