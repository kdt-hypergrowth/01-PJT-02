import requests
from pprint import pprint

def recommendation(title):
    pass
    # 영화 제목으로 검색을 하여 추천 영화 목록을 출력 
    # requests 라이브러리를 활용하여 TMDB에서 영화제목으로 영화를 검색(Search Movies)
    # 응답 받은 결과 중 첫번째 영화의 id 값을 활용하여 TMDB에서 추천 영화 목록(Get Recommendations)을 가져옵니다.
    # 추천 영화 목록을 리스트로 반환하는 함수를 작성
    
    # 여기에 코드를 작성합니다. 
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
    'api_key': '474c622ef9ff33b07a0bac17dd3e0ff2',
    'language': 'ko-KR',
    'query' : title
    }
    response = requests.get(BASE_URL+path,params=params).json().get('results')
    if len(response) == 0 :
        return None
    else :
        movie_id = response[0]['id']

    BASE_URL = 'https://api.themoviedb.org/3'
    path = f'/movie/{movie_id}/recommendations'
    params = {
        'api_key':'db73cdf92f64511f998356227c82b682',
        'language':'ko-KR'
    }
    response = requests.get(BASE_URL+path,params=params).json().get('results')
    result = []
    for i in range(len(response)):
        result.append(response[i]['title'])
    return result

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
