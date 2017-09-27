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
consumer_key = '5z0sfk6FYOa6HQwsW50o2rcTc'
consumer_secret = '	uSf6mPLhqVew9QyWsFUp8N6cUEpBDRNwrU48hRpsMrJzOId7UK'
access_token_key = '912715351355383808-ExBFy5wIibRYYuKnjGRarHtzNxXPPnG'
access_token_secret = 'p4VlHmYZwSSUNakbUVz4xU0qrqdX8Vo2EkWXMMu7jkmfR'


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
    print(tweetBot_id+" "+tweetBot_screenName)
    tweetBot = LT.TweetBot(keys=keys, user_id=tweetBot_id)
    _thread.start_new_thread(tweetBot.get_last_tweet,('get_last_tweet',))

while True:
    time.sleep(10)