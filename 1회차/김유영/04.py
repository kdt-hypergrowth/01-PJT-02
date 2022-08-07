from bs4 import ResultSet
import requests
from pprint import pprint


def recommendation(title):
    BASE_URL = 'https://api.themoviedb.org/3'
    search = '/search/movie'
    # 영화 제목으로 영화 검색
    params = {
        'api_key' : '143e53e7e83b57a0c8376b3020cd5051',
        'language': 'ko',
        'query' : title
    }
# url를 통해 서버에 요청해서 응답받고, json타입 데이터를 dictionary타입으로 바꿔 변수에 저장
    response = requests.get(BASE_URL+search, params=params).json()
    results=[]
    # 실행에 검색 할 수 없는 결과를 빈 리스트로 변환하기 때문ㅁ에
    # 검색 가능한 결과값들을 모을 리스트 생성 
    if response['results']:
        movie_id = response['results'][0]['id']
    else:
        return None
    # 값을 변수를지정해주고 영화 검색에서 받은 결과중 첫번째 영화 id 값을 추천 영화 목록에 가져옴 

    BASE_URL ='https://api.themoviedb.org/3'
    path2 = f'/movie/{movie_id}/recommendations'
    params2 = {
        'api_key' : '143e53e7e83b57a0c8376b3020cd5051',
        'language': 'ko',
        'query': movie_id
    }
    response2 = requests.get(BASE_URL+path2, params2).json()
    for i in response2['results']:
        # 반복
        results.append(i['title'])
    return results



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
