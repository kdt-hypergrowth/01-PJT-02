import requests
from pprint import pprint


def recommendation(title):
    BASE_URL = 'https://api.themoviedb.org/3' # API URL 불러오기
    path = '/search/movie' # API URL 불러오기
    params = {
        'api_key' : '801b2f9c7a6d8dce6f3bd7f807c9ffc5', # 세부 정보
        'language' : 'ko-KR',
        'query' : title # 찾고자 하는 정보
    }
    response = requests.get(BASE_URL+path, params=params).json() # requests 받아옴

    if response['results']: # requests에 results가 있으면
        movie_id = response['results'][0]['id'] # results에 0번째 id 를 가져옴
        path2 = f'/movie/{movie_id}/recommendations' # movie_id 를 입력해서 api 받아옴
        params2 = {
            'api_key' : '801b2f9c7a6d8dce6f3bd7f807c9ffc5', # 세부 정보
            'language' : 'ko-KR',
            'query' : 'id' # 찾고자 하는 정보
        }
        response2 = requests.get(BASE_URL+path2, params=params2).json() # requests 받아옴
        recommand_results = response2.get('results')
        recommand = [movie.get('title') for movie in recommand_results] # 추천 리스트 영화를 목록으로 보여줌
        # 추천 영화가 없으면 빈 리스트로 나오게 됨

        return recommand # 추천 영화를 반환
   
    else: # results 가 없으면
        return None # none 반환
    

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
