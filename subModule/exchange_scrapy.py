import scrapy
from scrapy.http import Request
import requests
import json
import time
import telepot
import codecs
from googletrans import Translator
import json
import rdd_status
import _thread
# scrapy genspider quotes toscrape.com

class BinanceSpider(scrapy.Spider):
    name = 'binance'
    allowed_domains = ['https://support.binance.com/hc/en-us/sections/115000106672-New-Listings','http://bithumb.cafe/notice','http://bittrex.com/api/v2.0/pub/currencies/GetWalletHealth?_=1508076591239']
    start_urls = ['http://support.binance.com/hc/en-us/sections/115000106672-New-Listings','http://bithumb.cafe/notice','http://bittrex.com/api/v2.0/pub/currencies/GetWalletHealth?_=1508076591239']
    base_url = 'http://support.binance.com'

    i = 0
    def parse(self, resposne):
        def rdd_msg_handling(i):
            while True:
                rdd_msg, ask_number, bid_number = rdd_status.rdd_status()
                if ask_number < 5 or bid_number < 5:
                    sendToTelebot('RDD Alert \n' + rdd_msg)
                    time.sleep(600)
                time.sleep(60)

        _thread.start_new_thread(rdd_msg_handling,(self.i,))
        yield Request(url=self.allowed_domains[0], callback=self.parse_binance, dont_filter=True)
        yield Request(url=self.allowed_domains[1], callback=self.parse_bithumb, dont_filter=True)
        yield Request(url=self.allowed_domains[2], callback=self.parse_bittrex, dont_filter=True)

    def parse_binance(self, response):
        binance_listing_file = open('binance_listing', 'r+')
        binance_news = response.css('li.article-list-item > a::text').extract_first()
        detail_url = response.css('li.article-list-item > a::attr(href)').extract_first()
        file_contents =  binance_listing_file.readlines()[-1]
        file_contents = file_contents.split('#')
        prev_title, prev_url = file_contents
        prev = {'title' : prev_title,
                'url' : prev_url}
        yield prev
        if prev_title.strip() != binance_news.strip():
            print('bool')
            print(prev_title.strip() + ' ' + binance_news.strip())
            new_list = {'title': binance_news,
             'url': self.base_url + detail_url}
            yield new_list
            sendToTelebot(new_list['title'],new_list['url'])
            binance_listing_file.seek(0, 2)
            binance_listing_file.write('\n'+new_list['title']+'#'+new_list['url'])
        # repetition/home/hojae/Documents
        print(self.i)
        self.i += 1
        binance_listing_file.close()
        yield Request(url=response.url, callback=self.parse_binance, dont_filter=True)
        time.sleep(60)

    def parse_bithumb(self, response):
        try:
            bithumb_notice_file = open('bithumb_notice', 'r+')
            bithumb_news = Translator().translate(str(response.css("h3.entry-title > a::text").extract_first()),dest='en').text
            detail_url = response.css("h3.entry-title > a::attr(href)").extract_first()
            file_contents = bithumb_notice_file.readlines()[-1]
            file_contents = file_contents.split('#')
            prev_title, prev_url = file_contents
            prev = {'title': prev_title,
                    'url': prev_url}
            yield prev
            if prev_title != bithumb_news:
                new_list = {'title': bithumb_news,
                            'url': detail_url}
                print('bithumb news ' + bithumb_news)
                print('prev title ' + prev_title)
                print(str(prev_title != bithumb_news))
                yield new_list
                sendToTelebot(new_list['title'],new_list['url'])
                bithumb_notice_file.seek(0, 2)
                bithumb_notice_file.write('\n'+new_list['title'] + '#' + new_list['url'])

            # repetition
            print(self.i)
            self.i += 1
            bithumb_notice_file.close()
            yield Request(url=response.url, callback=self.parse_bithumb, dont_filter=True)
        except IndexError as e:

            print(e)

    def parse_bittrex(self, response):
        try:
            bittrex_notice_file = open('bittrex_wallets', 'r+')
            wallet_set = set()
            for coin in bittrex_notice_file.readlines():
                wallet_set.add(coin.strip('\n'))
            for coin in json.loads(response.text)['result']:
                if coin['Currency']['CurrencyLong'] not in wallet_set:
                    print(str(coin['Currency']['CurrencyLong']) + 'is added !')
                    sendToTelebot(str(coin['Currency']['CurrencyLong']) + ' is added in bittrex wallet!')
                    bittrex_notice_file.seek(0, 2)
                    bittrex_notice_file.write('\n'+coin['Currency']['CurrencyLong'])

            bittrex_notice_file.close()
            # get rdd status

            yield Request(url=response.url, callback=self.parse_bittrex, dont_filter=True)

        except IndexError as e:
            print(e)



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


