import requests, json
from pprint import pprint


def get_specific(coin_id):
    endpoint = 'https://api.coinmarketcap.com/v1/ticker/'+coin_id+'/'
    try:
        r = requests.get(endpoint)
        data = r.json()
        return data[0]['market_cap_usd']
    except:
        print('try again')


def get(symbol, data):
    for coin in data:
        if coin['symbol'] == symbol:
            return float(coin['market_cap_usd'])


def get_all():
    endpoint = 'https://api.coinmarketcap.com/v1/ticker/?limit=30'

    r = requests.get(endpoint)
    data = r.json()
    total = 0
    coins = ['BTC', 'ETH', 'LTC', 'XRP', 'BCH', 'ADA', 'XLM', 'NEO', 'EOS', 'MIOTA', 'XMR', 'DASH', 'XEM']
    for coin in coins:
        total += get(coin, data)
    print(total/(10**9))

get_all()
