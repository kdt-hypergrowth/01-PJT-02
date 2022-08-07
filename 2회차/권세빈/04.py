import requests
from pprint import pprint
from dotenv import load_dotenv
import os
load_dotenv()

def recommendation(title):
    try:
        URL = 'https://api.themoviedb.org/3'
        path = '/search/movie'
        params = {
            'api_key': os.environ.get('api_key'),
            'language': 'ko-KR',
            'query': title
        }
        response = requests.get(URL+path, params=params).json()
        search = response.get('results')[0].get('id')
        movie_id = search
        URL = 'https://api.themoviedb.org/3'
        path =f'/movie/{movie_id}/recommendations'
        params = {
            'api_key': '79d21b47771ad41e6e0ed5b1a8b503e7',
            'language': 'ko-KR',
        }
        response = requests.get(URL+path, params=params).json()
        recomm = (response.get('results'))
        list = []
        for i in recomm:
            r = i['title']
            list.append(r)
        return(list)
    except:
        pass


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
