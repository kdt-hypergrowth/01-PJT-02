from multiprocessing.sharedctypes import Value
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
path = f'movie/{movie_id}/credits'

params ={
    'api_key' : '48111d6a7e925f23ade4fee564bcbbc4',
    'language':'ko-KR'
}

response2 = requests.get(BASE_URL+path,params=params).json().get('cast')
response3 = requests.get(BASE_URL+path,params=params).json().get('crew')


cast_list = []
crew_list = []

for i in response2:
    if i.get('cast_id') < 10:
        cast_list.append(i.get('name'))

for j in response3:        
    
    if j.get('department') == 'Directing':
        crew_list.append(j.get('name'))
        
list = [{'cast' : cast_list},{'crew' : crew_list }]

print(list)
    

