import requests

order_currency = 'BTC'
payment_currency = 'KRW'
URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'

response = requests.get(URL).json()
data = response['data']
prev_closing_price = data['prev_closing_price']

print(prev_closing_price)