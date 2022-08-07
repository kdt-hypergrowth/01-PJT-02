# - 제공된 영화 제목을 검색하여 해당 영화의 출연진(`cast`) 그리고 스태프(`crew`) 중 연출진으로 구성된 목록만을 출력합니다.
# - requests 라이브러리를 활용하여 TMDB에서 영화제목으로 영화를 검색(Search Movies)합니다. # 04.py 에서 검색코드 가져옴 id 값까지 가지고 옴
# - 응답 받은 결과 중 첫번째 영화의 id 값을 활용하여 TMDB에서 해당 영화에 대한 출연진과 스태프 목록(Get Credits)을 가져옵니다.
# 1. credits 검색 & 목록 가져오기

# - 출연진 중 `cast_id` 값이 `10 미만`인 출연진만 추출하고, 연출진은 부서(`department`)가 `Directing` 인 데이터만 추출합니다.
# 2. if 문 써서 출연진과 연출진 각각 조건 달아서 데이터 추출하기
# - `cast` 와 `directing` 으로 구성된 딕셔너리 먼저 만들어 놓기. 추출된 값을 리스트에 넣어 value로 저장하고 출력하는 함수를 작성합니다.
# 3. cast, directing 으로 구성된 딕셔너리에 값 리스트로 출력
# {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'],
#  'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}


import requests
from pprint import pprint


def credits(title):
    
    def search():
        #### movie_id 검색기능
        try :
            URL = 'https://api.themoviedb.org/3'
            path = f'/search/movie'

            params = {
                'api_key': '66393cafe6777ee92a0cc513816794be',
                'language': 'ko-KR',
                'query' : {title}
            }

            response = requests.get(URL+path, params=params).json() # title을 입력하고 검색했을 떄 나오는 결과를 json으로 받음
            res = response['results']
            
            return res[0]['id']  # int
        except IndexError :
            print('None')  # str  # 검색 실패시 none 반환
            exit()
        ####

    def search_credits():
        URL = 'https://api.themoviedb.org/3'
        movie_id = search()
        path = f'/movie/{movie_id}/credits'

        params = {
                'api_key': '66393cafe6777ee92a0cc513816794be',
                'language': 'ko-KR',
        }

        response = requests.get(URL+path, params=params).json() # title을 입력하고 검색했을 떄 나오는 결과를 json으로 받음
        
        c1 = response.get('crew')
        cr = []
        for i in c1:
            if i['department'] == 'Directing':
                cr.append(i['name'])

        c2 = response.get('cast')
        ca = []
        for i in c2:
            if i['cast_id'] < 10:
                ca.append(i['name'])

        return {"cast" : ca, "crew" : cr}
    
    return search_credits()


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환 
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    # pprint(credits('검색할 수 없는 영화'))
    # None
