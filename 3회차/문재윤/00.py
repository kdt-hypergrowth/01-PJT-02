import requests

url = "https://api.bithumb.com/public/ticker/BTC_KRW"
prev_closing_price = {"Accept": "application/json"}

response = requests.get(url, prev_closing_price)

response = response.json()
data = response.get('data')
print(data.get('prev_closing_price'))

