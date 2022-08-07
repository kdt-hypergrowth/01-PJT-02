import requests


BASE_URL = 'https://api.themoviedb.org/3/'
path ='movie/popular'

params ={
    'api_key' : '48111d6a7e925f23ade4fee564bcbbc4',
}

response = requests.get(BASE_URL+path,params=params).json()

print(len(response.get('results')))