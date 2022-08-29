import json
import requests
from TELE_BOT.config import keys


class APIException(Exception):
    pass


class PriseConverter:
    @staticmethod
    def convert(base: str, quote: str, amount: str):

        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')


        #r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')

        r = requests.get(f'https://www.alphavantage.co/query?function=FX_DAILY&from_symbol={quote_ticker}&to_symbol={base_ticker}&apikey=SWJ0XTJCJT5E7KMK')

        response = r.json()
        print(response)

        sell_price = response["Time Series FX (Daily)"]["2022-08-29"]["1. open"]
        print(sell_price)

        total_base = sell_price

        #total_base = json.loads(r.content)[keys[base]]
        return total_base
