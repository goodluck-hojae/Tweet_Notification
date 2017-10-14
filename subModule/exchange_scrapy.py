import scrapy
from scrapy.http import Request
import requests
import json
import time
import telepot
import codecs
from googletrans import Translator
# scrapy genspider quotes toscrape.com

class BinanceSpider(scrapy.Spider):
    name = 'binance'
    allowed_domains = ['https://support.binance.com/hc/en-us/sections/115000106672-New-Listings','http://bithumb.cafe/notice']
    start_urls = ['http://support.binance.com/hc/en-us/sections/115000106672-New-Listings','http://bithumb.cafe/notice']
    base_url = 'http://support.binance.com'

    i = 0
    def parse(self, resposne):
        yield Request(url=self.allowed_domains[0], callback=self.parse_binance, dont_filter=True)
        yield Request(url=self.allowed_domains[1], callback=self.parse_bithumb, dont_filter=True)

    def parse_binance(self, response):
        binance_listing_file = open('binance_listing', 'r+')
        binance_news = response.css('li.article-list-item > a::text').extract()[0]
        detail_url = response.css('li.article-list-item > a::attr(href)').extract()[0]
        file_contents =  binance_listing_file.readlines()[-1]
        file_contents = file_contents.split('#')
        print(file_contents)
        prev_title, prev_url = file_contents
        prev = {'title' : prev_title,
                'url' : prev_url}
        yield prev
        if prev_title != binance_news:
            new_list = {'title': binance_news,
             'url': self.base_url + detail_url}
            yield new_list
            sendToTelebot(new_list)
            binance_listing_file.seek(0, 2)
            binance_listing_file.write('\n'+new_list['title']+'#'+new_list['url'])
        # repetition
        print(self.i)
        self.i += 1
        yield Request(url=response.url, callback=self.parse_bithumb, dont_filter=True)

    def parse_bithumb(self, response):
        try:
            bithumb_notice_file = open('bithumb_notice', 'r+')
            bithumb_news = Translator().translate(response.css("h3.entry-title > a::text").extract_first(),dest='en').text
            detail_url = response.css("h3.entry-title > a::attr(href)").extract_first()
            file_contents = bithumb_notice_file.readlines()[-1]
            file_contents = file_contents.split('#')
            print(file_contents)
            prev_title, prev_url = file_contents
            prev = {'title': prev_title,
                    'url': prev_url}
            yield prev
            if prev_title != bithumb_news:
                new_list = {'title': bithumb_news,
                            'url': detail_url}
                yield new_list
                sendToTelebot(new_list)
                bithumb_notice_file.seek(0, 2)
                bithumb_notice_file.write('\n'+new_list['title'] + '#' + new_list['url'])

            # repetition
            print(self.i)
            self.i += 1
            yield Request(url=response.url, callback=self.parse_binance, dont_filter=True)
            time.sleep(60)
        except IndexError as e:
            print(e)

TOKEN = '311962567:AAGzqgnoQrAsYpqB6lKHW5Rns9YsupyLp0s'  # sys.argv[1]  # get token from command-line
print(TOKEN)
teleBot = telepot.Bot(TOKEN)
translator = Translator()

# Telegram Send Messagedd
def sendToTelebot(result):
    tele_users = teleBot.getUpdates(offset=100000001)
    tele_userid_set = set()

    try:
        for tele_user in tele_users:
            tele_userid_set.add(tele_user['message']['chat']['id'])

        teleBot.sendMessage(chat_id=-1001147113830, text='%s' % result['title'] + '\n\n' + result['url'])
        # teleBot.sendMessage(chat_id=436399842, text='%s' % tweet) #test bot
    except telepot.exception.BotWasBlockedError as e:
        print(e)


