import requests
from pprint import pprint
order_currency="BTC"
payment_currency="KRW"
url=f"https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}"
response=requests.get(url).json()
pprint(int(response['data']['opening_price']))