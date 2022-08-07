from dotenv import load_dotenv
import os

import requests
from pprint import pprint


def credits(title):

    # 여기에 코드를 작성합니다.  
    load_dotenv()
    key = os.getenv('KEY')

    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': key,
        'query': title,
        'language': 'ko-KR'
    }
    response = requests.get(BASE_URL + path, params = params).json()

    if response['results']:
        movie_ID = response['results'][0]['id']
        path = f'/movie/{movie_ID}/credits'

        if 'query' in params:
            del params['query']
        response = requests.get(BASE_URL + path, params = params).json()

        if response['cast'] and response['crew']:  # 출연진, 연출진으로 구성된 목록만 출력
            result = {}  # 값을 담을 빈 딕셔너리 선언
            cast = list(map(lambda x: x['original_name'], filter(lambda x: x['cast_id'] < 10, response['cast'])))
            crew = list(map(lambda x: x['original_name'], filter(lambda x: x['department'] == 'Directing', response['crew'])))
            result['cast'] = cast
            result['crew'] = crew
        else:
            result = []

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
