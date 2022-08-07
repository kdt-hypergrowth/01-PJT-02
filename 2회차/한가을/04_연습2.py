
import requests 
from pprint import pprint

def recommendation(title):
    URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params ={
        'api_key' : 'd84fbf5eb517d499e6c3ce37311d4394',
        'language' : 'ko-KR',
        'query' : 'title'
    }
    response = requests.post(URL + path, params=params).json()
    result = []

    if response['results']:
        movie_id = response['results'][0]['id']
        path = '/movie/{movie_id}/recommendations'
        params = {
            'api_key' : 'd84fbf5eb517d499e6c3ce37311d4394',
            'language' : 'ko-KR',
        }
        response = requests.post(URL + path, params).json()

        if response['results']:
            for i in response['results']:
                result.append(i['title'])
                return result
            else:
                return None

if __name__ == '__main__':
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None