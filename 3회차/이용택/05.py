import requests
from pprint import pprint
from dotenv import load_dotenv
import os


def credits(title):
    load_dotenv()
    key = os.getenv('KEY')
    params = {
        'api_key' : key,
        'language' : 'ko',
        'query' : title
    }
    base_url = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    
    res = requests.get(base_url + path, params = params).json()
    if res['results']:
        movie_id = res['results'][0]['id']
        path = f'/movie/{movie_id}/credits'
        res = requests.get(base_url + path, params = params).json()
        
        cast = list(map(lambda x : x['name'], filter(lambda x : x['cast_id'] < 10 , res['cast'])))
        crew = list(map(lambda x : x['name'], filter(lambda x : x['department'] == 'Directing', res['crew'])))

        result ={}
        result['cast'] = cast
        result['crew'] = crew

    else:
        result = None

    return result    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
