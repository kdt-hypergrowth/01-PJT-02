import requests

url = "https://api.bithumb.com/public/ticker/BTC_KRW"

response = requests.get(url)
response.json()

data = response.json()

print(data.get('data').get('prev_closing_price'))