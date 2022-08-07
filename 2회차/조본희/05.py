import requests
import os
from dotenv import load_dotenv
from pprint import pprint


def credits(title):
    load_dotenv()
    key = os.getenv('KEY')
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'

    params = {
        'api_key': key,
        'language': 'ko-KR',
        'query': title
    }

    response = requests.get(BASE_URL + path, params=params).json()
    result = {'cast': [], 'crew': []}
    if response['results']:
        movie_id = response['results'][0]['id']
        path = f'/movie/{movie_id}/credits'

        params = {
            'api_key': 'b730b79937fc4c4e8a1d72531451f76b',
            'language': 'ko-KR',
            'movie_id': movie_id
        }

        response = requests.get(BASE_URL + path, params=params).json()
        for cast in response['cast']:
            if cast['cast_id'] < 10:
                result['cast'].append(cast['name'])
        for crew in response['crew']:
            if crew['department'] == 'Directing':
                result['crew'].append(crew['name'])
        return result
        
    else:
        return None


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
