import requests

def yesterday_btc():
    order_currency = 'BTC'
    payment_currency = 'KRW'

    URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'

    response = requests.get(URL)

    ans = response.json().get('data').get('prev_closing_price')

    return ans

if __name__ == '__main__':
 
    print( yesterday_btc() )