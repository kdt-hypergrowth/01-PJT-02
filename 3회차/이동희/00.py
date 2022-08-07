import requests as r
import pprint

URL = 'https://api.bithumb.com/public/ticker/BTC_KRW'
headers = {'Accept': 'application/json'}
response = r.get(URL, headers=headers).json()
pprint.pprint(int(response.get('data').get('prev_closing_price')))