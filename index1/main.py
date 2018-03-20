#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import json
import urllib2
from pprint import pprint
from datetime import datetime


# def get_specific(coin_id):
#     endpoint = 'https://api.coinmarketcap.com/v1/ticker/'+coin_id+'/'
#     try:
#         r = requests.get(endpoint)
#         data = r.json()
#         return data[0]['market_cap_usd']
#     except:
#         print('try again')


def get(symbol, data):
    for coin in data:
        if coin['symbol'] == symbol:
            return float(coin['market_cap_usd'])


def get_all():
    endpoint = 'https://api.coinmarketcap.com/v1/ticker/?limit=30'

    data = urllib2.urlopen(endpoint)
    content = data.read()
    parsed = json.loads(content)
    # r = requests.get(endpoint)
    # data = r.json()
    total = 0
    coins = ['BTC', 'ETH', 'LTC', 'XRP', 'BCH', 'ADA', 'XLM', 'NEO', 'EOS', 'MIOTA', 'XMR', 'DASH', 'XEM']
    for coin in coins:
        total += get(coin, parsed)
    return (total/(10**9))

def update():
    called = False
    while(True):
        now = datetime.now()
        if now.minute % 5 == 0 and not called:
            self.response.write(get_all())
            called = True
        if now.minute % 5 == 1:
            called = False


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Hello world")


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
