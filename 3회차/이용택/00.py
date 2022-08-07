import requests
from pprint import pprint

order_currency = 'BTC'
payment_currency = 'KRW'
url = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'

res = requests.get(url)

pprint(res.json()['data']['prev_closing_price'])