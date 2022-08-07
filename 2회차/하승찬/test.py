
import requests

from pprint import pprint
# base_url = 'https://api.themoviedb.org/3'  # During handling of the above exception, another exception occurred: url틀렸을때 
# path = '/movie/popular'                    # 인기있는 영화 목록

# params = { 
#             'api_key' : '9c84ae21c51581335eb9aca74793ddb9',
#             'language': 'ko-KR' #데이터 str을  한국어로 변경 
#             } # 'Invalid API key: You must be granted a valid key.' 키없으면 키필요해 


# response= requests.get(base_url+path,params=params).json()# request.get (가져올 주소 + api 키를 딕셔너리로 넣어서 인증) .json의 형태로 가져온다


# pprint(len(response.get('results')))
# print (response)
base_ulr ='https://api.themoviedb.org/3'
path = ('/GET/movie/550/review')
params = {
  'api_key' : '9c84ae21c51581335eb9aca74793ddb9',
  'language' : 'ko-KR'
}

response =requests.get(base_ulr + path,params=params)

data =response.json()
print(data)