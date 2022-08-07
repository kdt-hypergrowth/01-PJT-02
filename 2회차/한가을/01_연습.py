# 인기 영화 목록의 개수 출력
from pprint import pprint
from urllib import response
import requests

URL = 'https://api.themoviedb.org/3'
path = '/movie/popular'
params ={
    'api_key' : 'd84fbf5eb517d499e6c3ce37311d4394',
    'language' : 'ko-KR'
}
response = requests.get(URL + path, params = params).json()
# pprint(type(response)) <class 'dict'>
# pprint(response.get('results'))
data = response.get('results')

def count_keys(data):
    count = 0
    for i in enumerate(data):
        count += 1
    return count
print(count_keys(data))