import requests
from pprint import pprint
# 9917f46b6425e1df8108a68c4d9202b0

def credits(title):
    movie_id = search(title)
    if movie_id == None:
        return None
    BASE_URL='https://api.themoviedb.org/3'
    path= f'/movie/{movie_id}/credits'
    prams = {
            'api_key' : '9917f46b6425e1df8108a68c4d9202b0',
            'language': 'ko-KR'
        }  
    response = requests.get(BASE_URL+path, params=prams).json()  
    if response == None:
        return None
    else:
        casts = response.get('cast')
        crews = response.get('crew')
        movie_dict = {"cast":[], "crew":[]}
        for cast in casts:
            if cast.get('cast_id') < 10: # 캐스트 id가 10 미만
                movie_dict['cast'].append((cast.get('name'))) # cast에 이름추가
        for crew in crews:
            if crew.get('department') == "Directing": # 부서가 Directing
                movie_dict['crew'].append((crew.get('name'))) # crew에 이름추가
        return movie_dict   


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


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
