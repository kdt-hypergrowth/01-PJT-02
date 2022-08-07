# ae34f93c0dcff82c16eb8b18b5631edb
# https://api.themoviedb.org/3/movie/76341?api_key=<<api_key>>
import requests
BASE_URL = 'https://api.themoviedb.org/3'
path = '/movie/43261'
params = {
    'api_key' : 'ae34f93c0dcff82c16eb8b18b5631edb',
    'language' : 'ko-KR'
}

response = requests.get(BASE_URL+path, params=params).json()
print(response)