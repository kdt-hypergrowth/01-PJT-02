import os
from dotenv import load_dotenv
import requests
from pprint import pprint

load_dotenv()

# 영화 제목으로 검색을 하여 해당 영화의 출연진(cast) 그리고 스태프(crew) 중 '연출진'으로 구성된 목록만을 출력
# requests 라이브러리로 영화제목으로 검색
# 응답 받은 결과 중 첫 번째 영화의 id값을 활용하여 해당 영화에 대한 출연진과 스태프(cast and crew) 목록을 가져옴
# 출연진 중 cast_id 값이 10미만인 출연진만 추출하고,
# 연출진은 부서(department)가 directing인 데이터만 추출
# cast와 directing으로 구성된 딕셔너리에 추출된 값을 '리스트'에 출력하는 함수 작성

def credits(title):
    
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': 'e0c0d3622b43ae47c6135b0a8f2cb8f2',
        'language' : 'ko-KR',
        'query' : title      
    }
        
    response = requests.get(BASE_URL + path, params=params).json().get('results')
    
    if len(response) == 0:
        return 
    
    path_credits = f'/movie/{response[0].get("id")}/credits'
    params_2 = {
        'api_key': os.getenv('TMDB'),
        'language' : 'ko-KR'
    } 
    response_cast = requests.get(BASE_URL + path_credits, params = params_2).json().get('cast')
    response_crew = requests.get(BASE_URL + path_credits, params = params_2).json().get('crew')
    
    cast_list = []
    crew_list = []
    credit_info = {"cast" : cast_list  , "crew" : crew_list }
    
    for cast in response_cast:
        if cast.get('cast_id') < 10:
            credit_info["cast"] += [cast.get('name')]
           
    for crew in response_crew:
        if crew.get('department') == 'Directing':
            credit_info["crew"] += [crew.get('name')]
           
   
    return credit_info 
    
        
    


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
