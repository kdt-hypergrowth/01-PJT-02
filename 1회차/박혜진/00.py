import requests

order_curr = 'BTC'
payment_curr = 'KRW'
url = f'https://api.bithumb.com/public/ticker/{order_curr}_{payment_curr}'

response = requests.get(url)

data = response.json()

print(data.get('data').get('prev_closing_price'))