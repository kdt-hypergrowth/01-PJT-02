import requests
from pprint import pprint
# - 제공된 영화 제목을 검색하여 해당 영화의 출연진(`cast`) 그리고 스태프(`crew`) 중 연출진으로 구성된 목록만을 출력합니다.
# - requests 라이브러리를 활용하여 TMDB에서 영화제목으로 영화를 검색(Search Movies)합니다.
# - 응답 받은 결과 중 첫번째 영화의 id 값을 활용하여 TMDB에서 해당 영화에 대한 출연진과 스태프 목록(Get Credits)을 가져옵니다.
# - 출연진 중 `cast_id` 값이 `10 미만`인 출연진만 추출하고, 연출진은 부서(`department`)가 `Directing` 인 데이터만 추출합니다.
# - `cast` 와 `directing` 으로 구성된 딕셔너리에 추출된 값을 리스트로 출력하는 함수를 작성합니다.

def credits(title):
    mvsearch = f"search/movie?query={title}"
    url = f"https://api.themoviedb.org/3/movie/{mvsearch}"
    params = {
        'api_key': 'personal key value input',
        'language': 'ko-KR'
    }   
    res = requests.get(url, params = params).json() #목록반환
    dic = {}
    cast_li = []
    crew_li = []
    try:
        resp = res['results']
        mv_id =  resp[0]['id']
        
        url2 = f'https://api.themoviedb.org/3//movie/{mv_id}/credits'
        res2 = requests.get(url2, params=params).json()
        crew_li2 = res2.get('crew')
        cast_li2 = res2.get('cast')
        for i in crew_li2:
            if i.get('department') == 'Directing':
                crew_li.append(i.get('name'))
        for i in cast_li2:
            if i.get('cast_id') < 10:
                cast_li.append(i.get('name'))
            dic["cast"] = cast_li
            dic["crew"] = crew_li
    except:
        return None
    
    return dic


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
