from urllib import response
import requests
from pprint import pprint


def recommendation(title):
     # API를 받아올 주소
    BASIC_URL = 'https://api.themoviedb.org/3'
    # search 주소
    path = '/search/movie'
    # 내 api 키와 언어 설정
    params = {
      'api_key': 'ec5782cbc602381ddeeedd23dcf585b9',
      'language': 'ko',
      'region': 'KR',
      'query': title
    }
    # 영화 홈페이지 받아오기
    response = requests.get(BASIC_URL + path, params=params).json()
    
    # 홈페이지에서 리절트 정보를 받아온다
    if response.get('results'):
        # results에 첫번째로 id를 가져온다? 
        id1 = response.get('results')[0].get('id')
    # 그렇지 않다면 id1은 None
    else :
        id1 = None

    # movie id가 id1에 있다
    movie_id = id1
    # 추천 사이트 
    path2 = f'/movie/{movie_id}/recommendations'
    # 추천 홈페이지 받아오기;
    res = requests.get(BASIC_URL + path2, params=params).json()
    # 받아올 리스트 추가
    res_List = []
    
    # 만약 추천받아온 results가 NoNE이라면 
    # None 리턴
    if res.get('results') == None:
        return None
    # 추천 홈페이지에 results 값에 무비가 있다면 
    for movie in res.get('results'):
        # 만약 무비가 none이라면 추천목록 리스트에 none
        if movie == None:
            res_List = None
        else:
            # 그렇지 않다면 title을 추천목록 리스트에 추가해라
            # print(res_List)
            res_List.append(movie.get('title'))
    
    return res_List

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
