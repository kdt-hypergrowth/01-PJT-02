import requests
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()


def recommendation(title):
    pass 
    # 여기에 코드를 작성합니다.  
    # 영화 추천 목록
    api_key = os.getenv('api_key')
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key' : api_key,
        'language' : 'ko-KR',
        'query' : f'{title}'
    }
    response = requests.get(BASE_URL+path, params=params).json()
    movies = response.get('results')
    #pprint(movies)
    # id = 496243
    
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/496243/recommendations'
    params = {
        'api_key' : api_key,
        'language' : 'ko-KR',
    }
    response2 = requests.get(BASE_URL+path, params=params).json()
    movie = response2.get('results')
    #pprint(movie)
    title = []
    for t in movie:
        title.append(t.get("title"))
    print(title)
    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    #['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    #pprint(recommendation('그래비티'))
    #[]
    #pprint(recommendation('검색할 수 없는 영화'))
    #None
