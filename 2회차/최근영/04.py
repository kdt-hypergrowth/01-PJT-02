from queue import Empty
import re
import requests
from pprint import pprint


def recommendation(title):

    base_url = 'https://api.themoviedb.org/3/search/movie'
    params = {
        'api_key': 'f25f9449dadd6f959e63b7b058966cea',
        'language': 'ko-KR',
        'query' : title
    }
    response = requests.get(base_url,params=params).json()
    re_params = {
        'api_key': 'f25f9449dadd6f959e63b7b058966cea',
        'language': 'ko-KR',        
    }
    if response['results'] == []:
        return None
    else:
        reco_movie = []
        movies = response['results']
        if title == movies[0]['title']:
            reco_movie = movies[0]['id']
        else:
            return reco_movie
        
        if reco_movie == None:
            return reco_movie
        else:
            re_url = f'https://api.themoviedb.org/3/movie/{reco_movie}/recommendations'
            reco_response = requests.get(re_url, params=re_params).json()
            re_movies = reco_response['results']
            re_movie = []
            for movie in re_movies:
                re_movie.append(movie['title'])
            return re_movie

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
