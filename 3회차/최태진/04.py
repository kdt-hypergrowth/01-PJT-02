import requests
from pprint import pprint


def recommendation(title):
    #첫번째 영화 id값
    base_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key' : '7506ce2e3f3a4cad52958b2c8f243e2e',
        'langage' : 'ko-KR',
        'query' : 'title'
    }
    response = requests.get(base_URL+path, params=params).json()
    data = response.get('results')

    #첫 번째 영화의 id값을 받음
    movie_id = data[0].get('id')
    pprint(f'id {movie_id}')

    #추천 영화 정보
    path_1 = f'movie/{movie_id}/recommendations'
    params_1 = {
        'api_key' : '7506ce2e3f3a4cad52958b2c8f243e2e',
        'langage' : 'ko-KR',
    }

    response_1 = requests.get(base_URL+path_1, params=params_1).json()
    data_1 = response_1.get('results')

    
    rlist = []
    
    for i in data_1: # 정보 중 영화 제목만 가져오기
        title = i.get('title')
        rlist.append(title)

    return rlist



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
    #pprint(recommendation('그래비티'))
    # []
    #pprint(recommendation('검색할 수 없는 영화'))
    # None
