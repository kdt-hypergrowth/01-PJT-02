import requests

order_currency = "BTC"
payment_currency = "KRW"
url = f"https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}"

response = requests.get(url=url).json()
data = response["data"]
prevPrice = data["prev_closing_price"]

print(prevPrice)