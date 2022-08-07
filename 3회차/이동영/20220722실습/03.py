import requests

BASE_URL = 'https://api.themoviedb.org/3/'
path ='movie/popular'

params ={
    'api_key' : '48111d6a7e925f23ade4fee564bcbbc4',
    'language':'ko-KR'
}

response = requests.get(BASE_URL+path,params=params).json()

data = response.get('results')
data2 = sorted(data, key = lambda x: ( -x['vote_average']))
for i in range(0,5):
    print(data2[i])