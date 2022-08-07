import os
from dotenv import load_dotenv
import requests
from pprint import pprint

load_dotenv()

# 영화 제목으로 검색을 하여 추천 영화 목록을 출력
# TMDB에서 영화제목으로 영화를 검색(Search Movies)
# 추천 영화 목록을 리스트로 반환하는 함수 작성

def recommendation(title):
    
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': os.getenv('TMDB'),
        'language' : 'ko-KR',
        'query' : title      
    }
        
    response = requests.get(BASE_URL + path, params=params).json().get('results')
    if len(response) == 0:
        return 
    
    path_recommend = f'/movie/{response[0].get("id")}/recommendations'
    params_2 = {
        'api_key': 'e0c0d3622b43ae47c6135b0a8f2cb8f2',
        'language' : 'ko-KR'        
    }
    
    response = requests.get(BASE_URL + path_recommend, params=params_2).json().get('results')
    recommend_list = []
    for t in response:
        recommend_list += [t.get('title')]
    return recommend_list
    

        
    

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
