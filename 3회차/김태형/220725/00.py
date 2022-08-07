import requests

url = "https://api.bithumb.com/public/ticker/BTC_KRW"

headers = {"Accept": "application/json"}

response = requests.get(url, headers=headers)
responseJson = response.json()
resData = responseJson['data']

print(resData['prev_closing_price'])