import requests

order_currency = 'BTC'
payment_currency = 'KRW'
url = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'
response = requests.get(url).json()
coins = response.get('data').get('prev_closing_price')
print(coins)