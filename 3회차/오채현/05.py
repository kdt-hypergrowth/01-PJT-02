from dotenv import load_dotenv
import os
import requests
from pprint import pprint


def credits(title):
    pass 
    # 여기에 코드를 작성합니다.  
    
    load_dotenv()
    
    API_KEY = os.environ.get('TMDB_API_KEY')
    Base_Url = 'https://api.themoviedb.org/3'

    path = '/search/movie'

    params = {
        'api_key': API_KEY,
        'language': 'ko-KR',
        'query': title,
    }
    res = requests.get(Base_Url+path, params=params).json()

    if res['results']:
        movie_ID = res['results'][0]['id']
        path = f'/movie/{movie_ID}/credits'

        if 'query' in params:
            del params['query']
        res = requests.get(Base_Url+path, params=params).json()

        if res['cast'] and res['crew']:
            result = {}
            cast = list(map(lambda x: x['original_name'], filter(lambda x: x['cast_id'] < 10, res['cast'])))
            crew = list(map(lambda x: x['original_name'], filter(lambda x: x['department'] == 'Directing', res['crew'])))
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
