import requests

BASE_URL = 'https://api.themoviedb.org/3/'
path ='search/movie'
query = input("영화제목을 입력하세요")

params ={
    'api_key' : '48111d6a7e925f23ade4fee564bcbbc4',
    'language':'ko-KR',
    'query' : f'{query}'
}

response1 = requests.get(BASE_URL+path,params=params).json().get('results')

movie_id = response1[0].get('id')

BASE_URL = 'https://api.themoviedb.org/3/'
path = f'movie/{movie_id}/recommendations'

params ={
    'api_key' : '48111d6a7e925f23ade4fee564bcbbc4',
    'language' : 'kr_KR'
}
list = []

response2 = requests.get(BASE_URL+path,params=params).json().get('results')

for i in response2:
    list.append(i.get('original_title'))

print(list)


