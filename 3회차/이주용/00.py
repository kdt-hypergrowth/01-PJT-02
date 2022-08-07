import requests
url = url = "https://api.bithumb.com/public/ticker/BTC_KRW"
response = requests.get(url).json()
print(response.get('data').get('prev_closing_price'))
