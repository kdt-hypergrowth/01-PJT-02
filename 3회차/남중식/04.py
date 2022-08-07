import requests
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY_TOKEN = os.getenv('my_api_key')

def recommendation(title):
    pass 
    # 여기에 코드를 작성합니다.
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': API_KEY_TOKEN,
        'language': 'ko-KR',
        'query': title
    }

    response = requests.get(BASE_URL+path, params=params).json() 
    result = response.get('results')
    
    # 영화 이름 검색 결과 없을 시, None 반환
    if result == []:
        return None
    
    # 영화 이름 검색 첫번째 결과의 id 값
    res_id = result[0].get('id')
    movie_id = res_id
    
    BASE_URL2 = 'https://api.themoviedb.org/3'
    path2 = f'/movie/{movie_id}/recommendations'
    params2 = {
        'api_key': 'f813cc9773fb55369f6d3e1dae17ba81',
        'language': 'ko-KR',
        'query': title
    }
    
    response_for_recommend = requests.get(BASE_URL2+path2, params=params2).json()
    result_for_recommend = response_for_recommend.get('results')
    
    titles_for_recommend = []
    
    for result in result_for_recommend:
        titles_for_recommend.append(result.get('title'))
        
    if titles_for_recommend == []:
        return []
    else:
        return titles_for_recommend
     


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
