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

TOKEN = '311962567:AAGzqgnoQrAsYpqB6lKHW5Rns9YsupyLp0s'  # sys.argv[1]  # get token from command-line
print(TOKEN)
teleBot = telepot.Bot(TOKEN)
translator = Translator()
# Telegram Send Messagedd
def sendToTelebot(title, url=''):
    tele_users = teleBot.getUpdates(offset=100000001)
    print('lol')
    print(tele_users)
    tele_userid_set = set()


    try:
        for tele_user in tele_users:
            tele_userid_set.add(tele_user['message']['chat']['id'])

        teleBot.sendMessage(chat_id=434815326, text='%s' % title + '\n\n' + url)
        # teleBot.sendMessage(chat_id=436399842, text='%s' % tweet) #test bot
    except telepot.exception.BotWasBlockedError as e:
        print(e)


sendToTelebot('test')