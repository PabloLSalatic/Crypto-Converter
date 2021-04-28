import requests
import traceback
import sys


class Crypto:

    def __init__(self, currency, cryptocurrency):
        self.currency = currency
        self.cryptocurrency = cryptocurrency

    def convert(self, amount):
        api = requests.get(
            'https://api.coinbase.com/v2/exchange-rates?currency='+self.cryptocurrency)
        try:
            currentPrice = api.json()['data']['rates'][self.currency]
        except KeyError:
            print('no')
        if currentPrice:
            total = amount / float(currentPrice)
            total_rounded = round(total, 9)
            return total_rounded
        else:
            print('no')


fiat = input('please input fiat currency: ').upper()
coin = input('please input coin: ').upper()

trying = Crypto(fiat, coin)


value = trying.convert(1000)

print(value)
