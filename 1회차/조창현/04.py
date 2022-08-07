import requests
from pprint import pprint


def recommendation(original_title):
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': '238bc3228df973eb1c16fa9c8a4a18bc',
        'query': original_title
    }
    response = requests.get(BASE_URL+path, params=params).json()

    movie = response['results']
    movie_id = 0
    for m in movie:
        movie_id = m['id']
        break
    if movie_id == 0:
        return(None)

    BASE_URL = 'https://api.themoviedb.org/3'
    path = f'/movie/{movie_id}/recommendations'
    params = {
        'api_key': '238bc3228df973eb1c16fa9c8a4a18bc',
        'language': 'ko-KR'
    }
    response = requests.get(BASE_URL+path, params=params).json()
    
    movie_list = []
    movie = response['results']
    for m in movie:
        movie_list.append(m['title'])

    return(movie_list)



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
