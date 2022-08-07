import requests
from pprint import pprint

# 영화 제목으로 검색을 하여 추천 영화 목록을 출력합니다.
# requests 라이브러리를 활용하여 TMDB에서 영화제목으로 영화를 검색(Search Movies)합니다.
# 응답 받은 결과 중 첫번째 영화의 id 값을 활용하여 TMDB에서 추천 영화 목록(Get Recommendations)을 가져옵니다.
# 추천 영화 목록을 리스트로 반환하는 함수를 작성합니다.

def recommendation(title):
    BASE_URL = 'https://api.themoviedb.org/3'
    search = '/search/movie'
    params = {
        'api_key' : '94ceed584568fa7a9113545f2e4291f5',
        'language' : 'ko-KR',
        'query' : title
    }
    # 영화 검색 BASE_URL에서 API request
    response = requests.get(BASE_URL+search, params=params)
    # 요청한 데이터를 json 형태로 가져온 후 'results'에 해당하는 값들을 저장
    movies = response.json().get('results')

    try:
        # title에 해당하는 검색 결과의 첫번째 데이터의 'id' 저장
        id = movies[0]['id']
        # 검색할 수 없는 영화이면 None 저장하도록 예외처리
    except IndexError:
        id = None
    
    recommand1 = '/movie/'
    movie_id = str(id)
    recommand2 = '/recommendations'
    params = {
            'api_key' : '94ceed584568fa7a9113545f2e4291f5',
            'language' : 'ko-KR'
        }

    # 영화 추천 BASE_URL에서 해당 id에 맞는 추천 API request
    response = requests.get(BASE_URL+recommand1+movie_id+recommand2, params=params)
    # 요청한 데이터를 json 형태로 가져온 후 'results'에 해당하는 값들을 저장
    movies = response.json().get('results', None)

    # None으로 데이터가 넘어왔으면
    if movies == None:
        # None 출력
        return None

    # 빈 답지 리스트 생성
    ans = []
    
    # movies에 for문으로 반복하면서 접근
    for i in range(len(movies)):
        # movie의 'title' 추가
        ans.append(movies[i]['title'])
    return ans


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
