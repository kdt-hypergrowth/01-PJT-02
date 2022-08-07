import requests


def current_price():
    # 여기에 코드를 작성합니다. 
    order_currency = "BTC"
    payment_currency = "KRW"
    params = {
        "order_currency": order_currency,
        "payment_currency": payment_currency
    }

    baseURL = "https://api.bithumb.com/public/ticker/"
    response = requests.get(baseURL, params=params).json()

    return response["data"]["prev_closing_price"]


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(current_price())
    # 20
