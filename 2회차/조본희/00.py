import requests

url = "https://api.bithumb.com/public/ticker/BTC_KRW"

response = requests.get(url).json()

data = response['data']
prev_closing_price = data['prev_closing_price']

print(prev_closing_price)