import requests
import json

url = "https://api.bithumb.com/public/ticker/BTC_KRW"
headers = {"Accept": "application/json"}
response = requests.get(url, headers=headers)
strToJson = json.loads(response.text)
print(strToJson['data']['prev_closing_price'])