from TwitterSearch import *
from multiprocessing.pool import ThreadPool
import _thread
import time
import datetime, pytz

tso = TwitterSearchOrder()
tso.set_keywords(['since:'+str(time.gmtime().tm_year)+'-'+str(time.gmtime().tm_mon)+'-'+str(time.gmtime().tm_mday)], or_operator = True)
tso.add_keyword("from:dr_coder_kor")
# it's about time to create a TwitterSearch object with our secret tokens
ts = TwitterSearch(
    consumer_key='5z0sfk6FYOa6HQwsW50o2rcTc',
    consumer_secret='uSf6mPLhqVew9QyWsFUp8N6cUEpBDRNwrU48hRpsMrJzOId7UK',
    access_token='912715351355383808-ExBFy5wIibRYYuKnjGRarHtzNxXPPnG',
    access_token_secret='p4VlHmYZwSSUNakbUVz4xU0qrqdX8Vo2EkWXMMu7jkmfR'
)

def retrieveRecentTweet(tso):
    while 1:
        for tweet in ts.search_tweets_iterable(tso):
            tweet_time_info = tweet['created_at'].split(' ')
            now = datetime.datetime.now()

            tweet_time = datetime.datetime(int(tweet_time_info[5]),int(time.strptime(tweet_time_info[1],'%b').tm_mon),int(tweet_time_info[2]),
                                           int(tweet_time_info[3].split(':')[0]),int(tweet_time_info[3].split(':')[1]),int(tweet_time_info[3].split(':')[2]))

            #print(now)
            if abs((tweet_time - now).seconds-15*3600) < 30:
                print(abs((tweet_time - now).seconds-15*3600))
                print(tweet['created_at'].split(' '))
        time.sleep(5)
           #print('@%s tweeted: %s' % (tweet['user']['screen_name'], tweet['created_at']))


try:
    _thread.start_new_thread(retrieveRecentTweet,(tso,))
     # this is where the fun actually starts :)

    while 1:
        time.sleep(10)
except TwitterSearchException as e:  # catch all those ugly errors
    print(e)
