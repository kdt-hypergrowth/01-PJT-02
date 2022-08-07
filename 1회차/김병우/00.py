import requests

order_currency = "BTC" # 기본값
payment_currency = "KRW" # 원화
params = {
    "order_currency" : order_currency,
    "payment_currency" : payment_currency
} # params 딕셔너리 만듬

URL = "https://api.bithumb.com/public/ticker/"
r = requests.get(URL).json()
    
print(r["data"]["prev_closing_price"]) # 전일종가