from bs4 import BeautifulSoup
import requests
import json

coinmarketcap = requests.get('https://bittrex.com/api/v1.1/public/getmarkets')

data = coinmarketcap.text

market_result = json.loads(data)

coin_set = set()
for coin_info in market_result['result']:
    coin_set.add(coin_info['MarketCurrencyLong'])

coin_tweet_set = set()

for coin in coin_set:
    coinmarketcap_social = requests.get('https://coinmarketcap.com/currencies/'+coin+'/#social')
    data_social = coinmarketcap_social.text
    soup_social = BeautifulSoup(data_social,'html.parser')

    for link in soup_social.find_all('a'):
        if link.get('href') is not None and "twitter" in link.get('href'):
            if link.string.split('@')[1] != 'CoinMKTCap':
                coin_tweet_set.add(link.string.split('@')[1])
                print(link.string.split('@')[1])

#print(coin_tweet_set)

print(coin_tweet_set.difference('trustplus'))