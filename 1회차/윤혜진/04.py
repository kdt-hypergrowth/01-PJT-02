import requests
from pprint import pprint
from dotenv import load_dotenv
import os

def recommendation(title):
    load_dotenv()
    key = os.environ.get('TMDB_API_key')

    # 1) 검색한 영화를 조회한 후, 첫번째 영화의 id를 가져옴
    base_url = 'https://api.themoviedb.org/3'
    path1 = '/search/movie'
    prameters1 = {
        'api_key' : key,
        'language': 'ko-KR',
        'query':title,
        'page':1
    }
   
    response1 = requests.get(base_url + path1, params=prameters1).json()
    
    # 영화 제목으로 검색해, 찾아준 영화 목록을 출력
    search_rst = response1.get('results')   
    # 검색한 영화 제목이 존재하면, 첫번째 영화의 id값을 기록
    movie_id = 0
    if search_rst:
        movie_id = search_rst[0]['id']
    # 검색한 영화 제목이 존재하지 않으면 반환
    else:
        return None

    

    # 2) 특정 영화에 대한 추천 영화 목록 조회
    path2 = f'/movie/{movie_id}/recommendations'
    prameters2 = {
        'api_key' : '36e69126e5702e17a95125dc94bbccbe',
        'language': 'ko-KR',
        'page':1
    }
    
    response2 = requests.get(base_url + path2, params=prameters2).json()

    movies_info = response2.get('results')
    recommendation_movies = []
    for movie in movies_info:
        recommendation_movies.append(movie.get('title'))
    
    return recommendation_movies



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
