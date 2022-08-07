import requests

def get_btc_krw():
    order_currency = 'BTC'
    payment_currency = 'KRW'

    URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'

    response = requests.get(URL).json()
    prev_closing_price = response.get('data').get('prev_closing_price')
    
    return prev_closing_price


if __name__ == "__main__":
    print(get_btc_krw())
