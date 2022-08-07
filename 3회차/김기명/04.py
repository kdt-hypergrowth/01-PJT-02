import requests
from pprint import pprint


def recommendation(title):
    api_key = 'a709df78a1a09780128430e580888cb9'
    url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&language=en-US&page=1&include_adult=false'
    movie_id = 

    url = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key={api_key}&language=en-US&page=1'

    #세시간동안 아무것도 못하고 삽질만하다가 포기. 이시간에 swea라도 풀었다면.
    #쓰는양식도 모르겠고 뭐가뭔지 전혀모르겠는데 무작정 전부다 찾아서 하려니까 하다하다 더 못하겠어서 포기합니다
    #사실 앞의 문제들도 정말 시간이 오래걸렸는데 이렇게까지 해야하나 싶은 생각이 계속 들었어요

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
