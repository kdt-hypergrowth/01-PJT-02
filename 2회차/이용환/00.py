
import requests

URL = 'https://api.bithumb.com/public/ticker/BTC_KRW'
response = requests.get(URL).json()
data = response['data']
result = data['prev_closing_price']
print(result)