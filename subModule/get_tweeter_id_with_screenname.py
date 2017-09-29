import time
import tweepy

consumer_key = 'W26NNy6uylLp3mxqnV7cn8Qqz'
consumer_secret = '8sn8M4PGfMO8Xt1SYPCWyTVVWhHrhvl6LmTCXZKur641wKR9Ia'
access_token_key = '912715351355383808-OwpvxPRotKpCSUf9CprZrnsiBtUGPnG'
access_token_secret = 'b89R6GNbPnrYIV4lbDOs0eRgqnJerEczyMQckyc75ONGF'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

api = tweepy.API(auth)

twitter_list_file = open('twitter_list')
twitter_list = [x.strip() for x in twitter_list_file.readlines()]
for twitter in twitter_list:
    print(twitter)
    user = api.get_user(twitter)
    print(user.id)
