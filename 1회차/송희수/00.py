import requests

url = "https://api.bithumb.com/public/ticker/BTC_KRW"

headers = {"Accept": "application/json"}

response = requests.get(url, headers=headers)
data = response.json()
print(data.get('data').get('prev_closing_price'))