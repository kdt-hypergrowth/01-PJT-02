import requests

def get_btc_krw():
    order_currency = "BTC"
    payment_currency = "KRW"
    url = f"https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}"
    # url로 요쳥을 보내서
    res = requests.get(url=url).json()
    data = res["data"]
    # 응답받은 값을 가져온다..
    prev_closing_price = data["prev_closing_price"]

    return prev_closing_price


if __name__ == "__main__":
    print(get_btc_krw())