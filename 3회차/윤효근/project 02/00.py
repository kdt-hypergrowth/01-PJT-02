import requests

url = "https://api.bithumb.com/public/ticker/BTC_KRW"

headers = {"Accept": "application/json"}

response = requests.get(url, headers=headers)
test = response.json()
money = test['data']['closing_price']
print(money)
