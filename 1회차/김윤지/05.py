# - 제공된 영화 제목을 검색하여 해당 영화의 출연진(`cast`) 그리고 스태프(`crew`) 중 연출진으로 구성된 목록만을 출력합니다.
# - requests 라이브러리를 활용하여 TMDB에서 영화제목으로 영화를 검색(Search Movies)합니다.
# - 응답 받은 결과 중 첫번째 영화의 id 값을 활용하여 TMDB에서 해당 영화에 대한 출연진과 스태프 목록(Get Credits)을 가져옵니다.
# - 출연진 중 `cast_id` 값이 `10 미만`인 출연진만 추출하고, 연출진은 부서(`department`)가 `Directing` 인 데이터만 추출합니다.
# - `cast` 와 `directing` 으로 구성된 딕셔너리에 추출된 값을 리스트로 출력하는 함수를 작성합니다.

import requests
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv()
MV_API_KEY = os. environ.get("MV_API_KEY")

def credits(title):
     
    # 여기에 코드를 작성합니다.  
    MV_URL = 'https://api.themoviedb.org/3'   #
    path1 = '/search/movie'                   

    params = {
        'api_key': MV_API_KEY ,  
        'language': 'ko-KR' ,     
        'query': title             
     }
    # title로 검색한 결과 딕셔너리안의 results 리스트를 받아옴
    rsp = requests.get(MV_URL+path1, params=params).json().get('results')
    
    # 검색 결과가 없다면 None 반환
    if len(rsp) == 0:
        return None

    # 검색한 영화는 검색결과의 제일 첫번째 영화
    search_movie = rsp[0]

    # 검색한 영화의 id로 cast, crew 찾기 (Get Credits)
    MV_URL = 'https://api.themoviedb.org/3'
    path2 = '/movie/'+ str(rsp[0].get('id'))+'/credits'
    params = {
        'api_key': MV_API_KEY,
        'language': 'ko-KR',
    }

    # credit 정보 딕셔너리가 들어간 리스트
    rsp2 = requests.get(MV_URL+path2, params=params).json()

    cast_result = []
    crew_result = []

    # cast_id 값이 10 미만인 cast 추출
    cast = rsp2.get('cast')
    for i in cast:
        if i.get('cast_id') < 10:
            cast_result.append(i.get('name'))

    # department가 Directing인 crew 추출
    crew = rsp2.get('crew')
    for i in crew:
        if i.get('department') == 'Directing':
            crew_result.append(i.get('name'))

    return {"cast": cast_result, "crew": crew_result}

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
