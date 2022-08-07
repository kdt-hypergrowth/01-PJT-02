import requests
# 306674

BASE_URL = 'https://api.themoviedb.org/3'
path = '/movie/306674/credits'
params = {
    'api_key': 'e3ebcaf0cb86336e3fa61579f1f0569b',
    'language': 'ko-KR',
    }
    
res = requests.get(BASE_URL + path, params=params).json()

print(res)

