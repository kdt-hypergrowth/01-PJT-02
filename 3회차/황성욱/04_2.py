import requests
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)
key = os.getenv('key')


def recommendation(title):
    base = 'https://api.themoviedb.org/3'
    path = f'/search/movie'
    params = {
    'api_key': key,
    'language': 'ko-KR',
    'query' : title
    }
    li = []
    try:
        response = requests.get(base+path, params=params).json()
        res = response.get('results')[0].get('id')
        recom_path = f'/movie/{res}/recommendations'
        response2 = requests.get(base+recom_path, params=params).json()
        res2 = response2.get('results')
        
        rec = list(map(lambda x:x['title'], res2))

        return rec
    except:
        return None
    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
