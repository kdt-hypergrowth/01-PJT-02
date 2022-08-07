import requests
from pprint import pprint


def credits(title):
    try :
        base_url = 'https://api.themoviedb.org/3'  
        path = '/search/movie'
        params = {
        'api_key' : '01d26c653a736a722edb8d872c129e3d',
        'language': 'ko-KR',
        'query' : title
        } 
        resp = requests.get(base_url+path, params=params).json()['results'] #우선 title을 검색 한다
        movie_id = resp[0]['id'] #검색 결과로부터 id 값을 가져온다.

        path = f'/movie/{movie_id}/credits' #id로 credits 정보를 가져온다.
        params = {
        'api_key' : '01d26c653a736a722edb8d872c129e3d',
        'language': 'ko-KR'
        }
        resp_1 = requests.get(base_url+path, params=params).json()['cast'] # 출연진
        resp_2 = requests.get(base_url+path, params=params).json()['crew'] # 연출진
        cast = [] 
        crew = []
        for i in resp_1 : #출연진중 cast id가 10 미만인 사람들만 cast에 리스트로 저장한다.
            if int(i['cast_id']) < 10 :
                cast.append(i['name'])
        for i in resp_2 : #출연진중 department가 Directing 사람들만 crew에 저장한다.
            if i['department'] == 'Directing' :
                crew.append(i['name'])
    
    except : pass #검색 할 수 없는 영화일시 예외로 pass한다.
    else : return {"cast" : cast, "crew" : crew} #cast와 crew를 딕셔너리로 만들어 반환한다.


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
