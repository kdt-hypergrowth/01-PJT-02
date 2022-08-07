# - 영화 제목으로 검색을 하여 추천 영화 목록을 출력합니다.
# - requests 라이브러리를 활용하여 TMDB에서 영화제목으로 영화를 검색(Search Movies)합니다.
# - 응답 받은 결과 중 첫번째 영화의 id 값을 활용하여 TMDB에서 추천 영화 목록(Get Recommendations)을 가져옵니다.
# - 추천 영화 목록을 리스트로 반환하는 함수를 작성합니다. 

# movie_id = int

import requests
from pprint import pprint

def recommendation(title): # 영화를 검색하는 함수를 포함한 영화 추천 함수
    
    def search():   # 영화를 검색하는 함수
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
            print('None')  # str
            exit()

    URL = 'https://api.themoviedb.org/3'
    movie_id = search()
    path = f'/movie/{movie_id}/recommendations'
    
    params = {
      'api_key': '66393cafe6777ee92a0cc513816794be',
      'language': 'ko-KR'
    }

    response = requests.get(URL+path, params=params).json()
    res = response['results']
    list0 = []

    for i in range(len(res)) :
        list0.append(res[i]['title'])

    return list0



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
