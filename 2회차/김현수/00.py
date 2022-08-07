# 0f810078345847f7d4b6930619626f55
# https://api.themoviedb.org/3/movie/550?api_key=0f810078345847f7d4b6930619626f55
# API 문서와 requests 활용 (연습)
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