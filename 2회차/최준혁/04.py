import requests
from pprint import pprint

# 검색
def search(title):
    movie_id = None
    BASE_URL='https://api.themoviedb.org/3'
    path='/search/movie'
    prams = {
            'api_key' : '9917f46b6425e1df8108a68c4d9202b0',
            'language': 'ko-KR', 
            'query': f'{title}' # 입력한 타이틀 값 검색
        } 
    response = requests.get(BASE_URL+path, params=prams).json()
    # 검색실패시
    if response == None: # 찾을 수 없는 값이 나올경우 None
        return None
    else:
        results = response.get('results') # 조회결과값 반환(리스트)
        for x in range(len(results)):
            movie_id = results[0].get('id') 
        return movie_id


def recommendation(title):
    movie_id = search(title) # 타이틀을 검색을 하면(title)값이 들어가 search로 보내짐
    if movie_id == None:
        return None
    BASE_URL='https://api.themoviedb.org/3'
    path=f'/movie/{movie_id}/recommendations'
    prams = {
            'api_key' : '9917f46b6425e1df8108a68c4d9202b0',
            'language': 'ko-KR'
        }
    
    response = requests.get(BASE_URL+path, params=prams).json()
    if response == None:
        return None
    else: 
        results = response.get('results')
        recommend_list = []
        for result in results:
            movie = result.get('title')
            recommend_list.append(movie)
        return recommend_list

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
