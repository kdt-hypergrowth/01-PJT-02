import requests

order_currency = "BTC"
payment_currency = "KRW"
url = f"https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}"

res = requests.get(url).json()
data = res.get('data')
prev_closing_price = data.get('prev_closing_price')

print(prev_closing_price)