import requests

order_currency = 'BTC'
payment_currency = 'KRW'
URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'
response = requests.get(URL).json()
closing_price = response.get('data').get('closing_price')
print(response.get('data').get('closing_price'),closing_price)