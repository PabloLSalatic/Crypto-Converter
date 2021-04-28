import requests


class Cryptoconvert:

    def __init__(self, currency, cryptocurrency, amount):
        self.currency = currency
        self.cryptocurrency = cryptocurrency
        self.amount = amount

    def convert(self, amount):
        api = requests.get(
            'https://api.coinbase.com/v2/exchange-rates?currency='+self.cryptocurrency)
        try:
            currentPrice = api.json()['data']['rates'][self.currency]
        except KeyError:
            print('Error, revise los valores.')
        if currentPrice:
            total = amount / float(currentPrice)
            total_rounded = round(total, 6)
            return total_rounded
        else:
            print('Error, revise los valores.')
        print(self.amount)


if __name__ == '__main__':
    currency = input('Ingrese moneda (ejemplo, USD): ').upper()
    cryptocurrency = input('Ingrese moneda (ej: BTC) ').upper()
    amount = int(input(f'Ingrese cantidad de dinero {currency}: ').upper())

call_crypto = Cryptoconvert(currency, cryptocurrency, amount)
final_value = call_crypto.convert(amount)
print(f'El total es: {final_value} {cryptocurrency}')
