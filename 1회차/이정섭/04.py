import requests
from pprint import pprint


def recommendation(title):
    movie_id = search(title)
    if movie_id == None:
        return None
     
    Base_URL = 'https://api.themoviedb.org/3'
    path = f'/movie/{movie_id}/recommendations'
    params = {
    'api_key': '223131069bc4ff601e73529b7eb1b275'
              }

    response = requests.get(Base_URL+path, params=params).json()

    if response == None:
        return None
    else: 
        results = response.get('results')
        recommend_list = []
        for result in results:
            movie = result.get('title')
            recommend_list.append(movie)
        return recommend_list

def search(title):
    movie_id = None
    Base_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
    'api_key': '223131069bc4ff601e73529b7eb1b275',
    'query': f'{title}'
              }

    response = requests.get(Base_URL+path, params=params).json()

    if response == None:
        return None
    else:
        results = response.get('results')
        for x in range(len(results)):
            movie_id = results[0].get('id') 
        return movie_id
    
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
