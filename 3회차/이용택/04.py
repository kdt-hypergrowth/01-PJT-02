import re
import requests
from pprint import pprint
from dotenv import load_dotenv
import os

def recommendation(title):
    load_dotenv()
    key = os.getenv('KEY')
    params = {
        'api_key' : key,
        'language' : 'ko',
        'query' : title
    }
    base_url = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    
    res = requests.get(base_url + path, params = params)
    
    if res.json()['results']:
        movie_id = res.json()['results'][0]['id']
        path = f'/movie/{movie_id}/recommendations'
        res = requests.get(base_url + path, params = params).json()

        if res['results']:
            result = list(map(lambda x : x['title'], res['results']))
        else:
            result = []
    else:
        result = None
    
    return result

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))  # ok
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))