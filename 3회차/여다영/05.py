#05. 출연진 및 연출진 데이터 조회

#- 제공된 영화 제목을 검색하여 해당 영화의 출연진(`cast`) 그리고 스태프(`crew`) 중 연출진으로 구성된 목록만을 출력합니다.
#- requests 라이브러리를 활용하여 TMDB에서 영화제목으로 영화를 검색(Search Movies)합니다.
#- 응답 받은 결과 중 첫번째 영화의 id 값을 활용하여 TMDB에서 해당 영화에 대한 출연진과 스태프 목록(Get Credits)을 가져옵니다.
#- 출연진 중 `cast_id` 값이 `10 미만`인 출연진만 추출하고, 연출진은 부서(`department`)가 `Directing` 인 데이터만 추출합니다.
#- `cast` 와 `directing` 으로 구성된 딕셔너리에 추출된 값을 리스트로 출력하는 함수를 작성합니다.

#api_key : f4d88a36cfb682b86111c15f97a34324
#https://api.themoviedb.org/3/movie/550?api_key=f4d88a36cfb682b86111c15f97a34324
#GET/search/movie
#required : api_key, query
#GET/movie/{movie_id}/credits
#required : api_key

import requests
from pprint import pprint


def credits(title):
    pass 
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': 'f4d88a36cfb682b86111c15f97a34324',
        'query': title
    }

    response = requests.get(BASE_URL + path, params = params).json()
    results = response.get('results')

    if results:
        movie_id = results[0].get('id')
        
        path_2 = f'/movie/{movie_id}/credits'
        params_2 = {
            'api_key': 'f4d88a36cfb682b86111c15f97a34324'
        }

        cast = []
        crew = []
        credits = requests.get(BASE_URL + path_2, params = params_2).json()
        cast_list = credits.get('cast')
        crew_list = credits.get('crew')

        for i in cast_list:
            if i['cast_id'] < 10:
                cast.append(i['name'])
        
        for i in crew_list:
            if i['department'] == 'Directing':
                crew.append(i['name'])

        total_list = dict()
        total_list['cast'] = cast
        total_list['crew'] = crew

        return total_list
    else:
        return None


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
