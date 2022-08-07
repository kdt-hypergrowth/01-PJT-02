import requests

order_currency = 'BTC'
payment_currency = 'KRW'

url = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'

response = requests.get(url)
data = response.json()

print(data.get('data').get('closing_price'))
