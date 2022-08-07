# import requests
# url = "https://api.bithumb.com/public/ticker/BTC_KRW"
# headers = {"Accept": "application/json"}
# response = requests.get(url, headers=headers)
# print(response.text)

# prev_closing_price	전일종가	Number (String)

# BTC(비트코인)의 KRW(원) 전일종가
# output = 29812000


from urllib import response
import requests

order_currency = "BTC"
payment_currency = "KRW"
URL = f"https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}"

response = requests.get(URL)
data = response.json()

print(data.get('data').get('prev_closing_price'))
