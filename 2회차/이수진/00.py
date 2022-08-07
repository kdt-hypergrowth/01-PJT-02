import requests


def get_btc_krw():
    order_currency = "BTC"
    payment_currency = "KRW"
    url = f"https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}"

    response = requests.get(url).json()
    data = response["data"]
    prevPrice = data["prev_closing_price"]

    return prevPrice


if __name__ == "__main__":
    print(get_btc_krw())