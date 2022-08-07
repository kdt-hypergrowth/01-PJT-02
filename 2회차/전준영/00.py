import requests

url = f"https://api.bithumb.com/public/ticker/BTC_KRW"

headers = {"Accept": "application/json"}

response = requests.get(url).json()

print(response.get("data").get("closing_price"))