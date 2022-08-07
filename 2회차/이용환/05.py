from ast import Dict
import requests
from pprint import pprint


def credits(title):
    pass 
    # 여기에 코드를 작성합니다.  
    try:
        URL = 'https://api.themoviedb.org/3'
        movie = '/search/movie'
        params = { 'api_key' : '896988be1c1bb3801b7d75f69bd7b9a5', 'language' : 'ko-KR', 'query' : title}
        result = requests.get(URL+movie, params = params).json()
        a = result['results']
        movi = a[0]['id'] # 입력값 id 번호 찾기

        movie2 = f'/movie/{movi}/credits'
        params = { 'api_key' : '896988be1c1bb3801b7d75f69bd7b9a5', 'language' : 'ko-KR'}
        result2 = requests.get(URL+movie2, params = params).json()
        cast = result2['cast'] #cast 만 모으기
        cast2 = []
        for i in range(len(cast)):
            if cast[i]['cast_id'] < 10:
                cast2.append(cast[i]['name'])
        crew = result2['crew'] #crew 만 모으기
        crew2 = []
        for i in range(len(crew)):
            if crew[i]['department'] == 'Directing':
                crew2.append(crew[i]['name'])
        
        cast_crew = {'cast' : None, 'crew' : None} # 딕셔너리 생성
        cast_crew['cast'] = cast2 # 키 cast 안에 값 id 가 10 미만인 사람 이름만 모아서 추가
        cast_crew['crew'] = crew2 # 키 crew 안에 값 Directing 사람 이름만 모아서 추가
        return cast_crew # 반환 값 딕셔너리
    except IndexError:
        return None # 오류날시 None 출력

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
