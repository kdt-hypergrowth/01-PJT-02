import requests
from pprint import pprint


def recommendation(title):
    pass 
    # 여기에 코드를 작성합니다.
    Base_URL = "https://api.themoviedb.org/3/"
    path = 'search/movie'
    params = {
        'api_key': 'c88039a3ac8630f316e088cdecaae57a',
        'language': 'ko-KR',
        'query' : title
    }

    response =requests.get(Base_URL+path, params=params).json()
    results = []
    if response['results']:
        movie_id = response['results'][0]['id']    #첫번째 영화 id값을 넣어준다
    else:
        return None
    #추천영화가 없을 경우 []를 반환하며 검색에 실패할 시 none을 반환하게함



    BASE_URL ='https://api.themoviedb.org/3'
    paths = f'/movie/{movie_id}/recommendations'
    paramss = {
        'api_key' : 'c88039a3ac8630f316e088cdecaae57a',
        'language': 'ko-KR',
        'query': movie_id
    }
    responses = requests.get(BASE_URL+paths, paramss).json()
    for i in responses['results']:
        results.append(i['title'])
    return results


    #실패했습니다... []와 None이 연이어서 뜨는데 리턴을 어떻게 수정해야 할지...pprint를 지워서 가시적으로만 해결했습니다...하하...


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