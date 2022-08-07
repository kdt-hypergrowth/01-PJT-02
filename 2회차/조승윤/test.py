import requests
BASE_URL = 'https://api.themoviedb.org/3'
path = '/movie/43261'
# api_key 발급받아서 각자 키를 넣어주세요.
params = {
    'api_key': '9ceb4d4268730f0fa5cc90ef67abfc71',
    'language': 'ko-KR'
}

response = requests.get(BASE_URL+path, params=params).json()
print(response)