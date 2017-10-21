import scrapy
from scrapy.http import Request
import requests
import json
import time
import telepot
import codecs
from googletrans import Translator
import json
import _thread
import rdd_status
import ccxt
TOKEN = '311962567:AAGzqgnoQrAsYpqB6lKHW5Rns9YsupyLp0s'  # sys.argv[1]  # get token from command-line
print(TOKEN)
teleBot = telepot.Bot(TOKEN)
translator = Translator()
# Telegram Send Messagedd
def rdd_msg_handling():
    i=0
    while True:
        rdd_msg, ask_number, bid_number = rdd_status.rdd_status()
        print(rdd_msg)
        if ask_number < 5 or bid_number < 5:
            sendToTelebot('RDD Alert \n' + rdd_msg)
            print('RDD Alert!')
            time.sleep(600)
            i+=1
        print(rdd_msg)
        time.sleep(60)


def sendToTelebot(title, url=''):
    tele_users = teleBot.getUpdates(offset=100000001)
    tele_userid_set = set()


    try:
        for tele_user in tele_users:
            tele_userid_set.add(tele_user['message']['chat']['id'])
        teleBot.sendMessage(chat_id= -1001137040292, text='%s' % title + '\n\n' + url)
        teleBot.sendMessage(chat_id= -1001147113830, text='%s' % title + '\n\n' + url)
        print('testd')
        # teleBot.sendMessage(chat_id=436399842, text='%s' % tweet) #test bot
    except telepot.exception.BotWasBlockedError as e:
        print(e)

rdd_msg_handling()
