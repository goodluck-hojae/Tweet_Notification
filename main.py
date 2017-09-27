import sys
import time
import telepot
from telepot.loop import MessageLoop
import _thread
import datetime
from pprint import pprint
import TweetBot as LT

#Twitter Auth

# it's about time to create a TwitterSearch object with our secret tokens
consumer_key = 'W26NNy6uylLp3mxqnV7cn8Qqz'
consumer_secret = '	8sn8M4PGfMO8Xt1SYPCWyTVVWhHrhvl6LmTCXZKur641wKR9Ia'
access_token_key = '912715351355383808-OwpvxPRotKpCSUf9CprZrnsiBtUGPnG'
access_token_secret = 'b89R6GNbPnrYIV4lbDOs0eRgqnJerEczyMQckyc75ONGF'


keys = [consumer_key, consumer_secret, access_token_key, access_token_secret]

twitter_id_file = open('twitter_id')

twitter_name_with_ids = [x.strip() for x in twitter_id_file.readlines()]
print(twitter_name_with_ids)

tweetBot = LT.TweetBot(keys=keys, user_id=896471765047664640)
_thread.start_new_thread(tweetBot.get_last_tweet,('get_last_tweet',))
tweetBot = LT.TweetBot(keys=keys, user_id=912715351355383808)
_thread.start_new_thread(tweetBot.get_last_tweet,('get_last_tweet',))

for idx,twitter_name_with_id in enumerate(twitter_name_with_ids):
    tweetBot_screenName, tweetBot_id = twitter_name_with_id.split(' ')
    print(str(idx)+' '+tweetBot_id+" "+tweetBot_screenName)
    tweetBot = LT.TweetBot(keys=keys, user_id=tweetBot_id)
    _thread.start_new_thread(tweetBot.get_last_tweet,('get_last_tweet',))

while True:
    time.sleep(10)