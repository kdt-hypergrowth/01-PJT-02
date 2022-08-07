import requests
BASE_URL = 'https://api.themoviedb.org/3'
path = '/movie/now_playing'
# api_key 발급받아서 각자 키를 넣어주세요.
params = {
    'api_key': '223131069bc4ff601e73529b7eb1b275',
  }

response = requests.get(BASE_URL+path, params=params).json()

# print(response['results' >= str(8)])

# string 으로 변환 하지 않고 숫자 8을 주면 str/int error 때문에 str 변환을 해줬는데 keyerror: True 를 값으로 주고 있다. 
# I need 'vote_result' above 8 from 'results' 
# How can I make a list for the 'results' and choose the value i want

# Lambda and filter in Python Examples
# https://www.geeksforgeeks.org/lambda-filter-python-examples/