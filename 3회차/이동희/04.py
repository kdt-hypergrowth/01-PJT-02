import requests as r
from pprint import pprint
from dotenv import load_dotenv
import os 

load_dotenv()

def recommendation(title):
    pass 
    # 여기에 코드를 작성합니다.  
    base_url = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': os.environ.get('api_key'),
        'language': 'ko-KR',
        'query': {title}
    }
    response = r.get(base_url+path, params=params).json()
    response = response['results']
    
    try:
        movie_id = ((response[0])['id'])
        recommend_path = f'/movie/{movie_id}/recommendations'
        recommend_params = {
            'api_key': os.environ.get('api_key'),
            'language': 'ko-KR'
        }
        movie = r.get(base_url+recommend_path, params=recommend_params).json()
        movie = movie['results']
        recommend_list = []
        for title in movie:
            recommend_list.append(title['title'])
        return recommend_list
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
