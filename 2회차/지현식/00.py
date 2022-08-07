import requests

url = 'https://api.bithumb.com/public/ticker/'

response = requests.get(url).json()
print(response.get('data').get('prev_closing_price'))