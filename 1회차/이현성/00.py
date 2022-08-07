# from urllib import response
# import requests

# order_currency = 'ALL'
# payment_currency = 'KRW'
# URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'

# response = requests.get(URL).json()
# coins = response.get('data')

# for coin in coins:
#     if coins == 'date':
#         continue
#     print(coin, coins.get(coin).get('closing_price').get(str('BTC')))
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