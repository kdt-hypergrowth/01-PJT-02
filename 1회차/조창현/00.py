
import requests
from pprint import pprint

order = 'BTC'
payment = 'KRW'
URL = f'https://api.bithumb.com/public/ticker/{order}_{payment}'

response = requests.get(URL)

print(response, type(response))
print(response.text, type(response.text))
pprint(response.json())
print('=====================================================')
data = response.json()
print(data.get('data').get('prev_closing_price'))