# import requests

# #url
# order_currency = 'BTC'
# payment_currency = 'KRW'
# url = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'
# # 요청을 보내서
# response = requests.get(url)
# # 응답받을 값 가져오기 
# data = response.json()
# print(data)

import requests


def get_btc_krw():
    order_currency = "BTC"
    payment_currency = "KRW"
    url = f"https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}"

    res = requests.get(url=url).json()
    data = res["data"]
    prev_closing_price = data["prev_closing_price"]

    return prev_closing_price


if __name__ == "__main__":
    print(get_btc_krw())