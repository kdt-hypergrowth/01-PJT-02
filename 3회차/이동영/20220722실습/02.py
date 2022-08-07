import requests

BASE_URL = 'https://api.themoviedb.org/3/'
path ='movie/popular'

params ={
    'api_key' : '48111d6a7e925f23ade4fee564bcbbc4',
    'language': 'kr-KR'
}

response = requests.get(BASE_URL+path,params=params).json()

data = response.get('results')

for i in data:
    if  i.get('vote_average') >= 8.0:
        print(i)