import requests

order_currency = 'BTC'
payment_currency = 'KRW'

URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'

requests = requests.get(URL)
# prev_closing_price
date = requests.json()
print(date.get('data').get('prev_closing_price'))