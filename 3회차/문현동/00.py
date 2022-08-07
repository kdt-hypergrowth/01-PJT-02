from attr import asdict
import requests
from dotenv import load_dotenv

order_currency = "BTC"
payment_currency = "KRW"

url = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'

response = requests.get(url).json()

prev_closing_price = response.get("data").get("prev_closing_price")

print(prev_closing_price)