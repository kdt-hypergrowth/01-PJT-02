# 8854669b886a6c07c12ea947bcc2311d
# https://api.themoviedb.org/3/movie/76341?api_key=<<api_key>>
import requests
BASE_URL = 'https://api.themoviedb.org/3'
path = '/movie/popular'
# api_key 발급받아서 각자 키를 넣어주세요.
params = {
    'api_key': '223131069bc4ff601e73529b7eb1b275',
    'language': 'ko-KR'
}

response = requests.get(BASE_URL+path, params=params).json()
print(response)