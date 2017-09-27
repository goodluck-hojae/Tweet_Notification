import sys
import time
import telepot
from telepot.loop import MessageLoop
from TwitterSearch import *
import _thread
import datetime
from pprint import pprint

#Twitter Auth

tso = TwitterSearchOrder()
print('since:'+str(datetime.datetime.now().year)+'-'+str(datetime.datetime.now().month)+'-'+str(datetime.datetime.now().day))
with open("twitter_list") as f:
    twitter_list = f.readlines()
twitter_list = ['from:'+x.strip() for x in twitter_list]
twitter_list.append('from:dr_coder_kor')
twitter_list.append('from:leehoo31')
twitter_list.append('from:ulllbo')
twitter_list_candidate = twitter_list[0:20]
filter = ['since:'+str(time.gmtime().tm_year)+'-'+str(time.gmtime().tm_mon)+'-'+str(time.gmtime().tm_mday)]+twitter_list_candidate
tso.set_keywords(filter, or_operator=True)

# it's about time to create a TwitterSearch object with our secret tokens
ts = TwitterSearch(
    consumer_key='W26NNy6uylLp3mxqnV7cn8Qqz',
    consumer_secret='8sn8M4PGfMO8Xt1SYPCWyTVVWhHrhvl6LmTCXZKur641wKR9Ia',
    access_token='912715351355383808-OwpvxPRotKpCSUf9CprZrnsiBtUGPnG',
    access_token_secret='b89R6GNbPnrYIV4lbDOs0eRgqnJerEczyMQckyc75ONGF'
)

TOKEN = sys.argv[1]  # get token from command-line
bot = telepot.Bot(TOKEN)

def retrieveRecentTweet(tso):
    for tweet_content in ts.search_tweets_iterable(tso):
        tweet_time_info = tweet_content['created_at'].split(' ')
        now = datetime.datetime.now()

        tweet_time = datetime.datetime(int(tweet_time_info[5]),int(time.strptime(tweet_time_info[1],'%b').tm_mon),int(tweet_time_info[2]),
                                       int(tweet_time_info[3].split(':')[0]),int(tweet_time_info[3].split(':')[1]),int(tweet_time_info[3].split(':')[2]))

        print(tweet_time)
        print(now)
        if abs((tweet_time - now).seconds) < 300:
            print(abs((tweet_time - now).seconds))
            print('@%s tweeted: %s' % (tweet_content['user']['screen_name'], tweet_content['text']))
            return tweet_content['user']['screen_name'], tweet_content['text']
        return None, None


# Telegram Send Message
def sendToTelebot(tso, twitter_list):
    prev_tweet = None
    i=0;
    while True:
        print(i)
        twitter_list_candidate = twitter_list[19*i:19*(i+1)]
        if i != 10:
            tso.set_keywords(filter, or_operator=True)
        else:
            tso.set_keywords(filter, or_operator=True)
        user, tweet = retrieveRecentTweet(tso)
        tele_users = bot.getUpdates(offset=100000001)
        tele_userid_set = set()

        for tele_user in tele_users:
            tele_userid_set.add(tele_user['message']['chat']['id'])
        print(user)
        print(tweet)
        if user is not None and prev_tweet != tweet:
            for user_id in tele_userid_set :
                bot.sendMessage(user_id, user+' '+tweet)
                #bot.sendMessage(436399842, user+' '+tweet)
            print(' '+user+' '+tweet)
        prev_tweet = tweet
        time.sleep(20)
        i += 1
        if i == 10:
            i = 0

_thread.start_new_thread(sendToTelebot,(tso, twitter_list))
#MessageLoop(bot, sendToTelebot).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)