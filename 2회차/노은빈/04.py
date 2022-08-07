from re import I
import requests
from pprint import pprint

def recommendation(title):
    
    # 여기에 코드를 작성합니다.  
    base_url = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': '8b431f95b8d1aca3b694e017ecd9c4fb',
        'language': 'ko-KR',
        'query': title
    }

    response = requests.get(base_url + path, params=params).json()  
    movies = response.get('results')

    if response == None:
        return None  #None 반환
    else:
        movie_id = movies[0]['id']  
        #영화 검색 결과 중 첫번째 영화를 id 값을 이용해 추천 목록으로 가져와 그 값을 변수로 지정

    base_url = 'https://api.themoviedb.org/3'
    path = f'/movie/{movie_id}/recommendations'
    #f를 넣어야 변수 적용이 된다
    params = {
        'api_key': '8b431f95b8d1aca3b694e017ecd9c4fb',
        'language': 'ko-KR'
    }

    response = requests.get(base_url + path, params=params).json()  
    movies = response.get('results')
    result = []  #추천 영화 목록을 리스트로 반환

    for i in movies:
        title = i.get('title')
        result.append(title)  #result에 title 값만 추가
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