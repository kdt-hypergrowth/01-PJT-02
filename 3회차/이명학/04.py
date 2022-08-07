import requests
from pprint import pprint


def recommendation(title):
    pass

    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    # 영화 제목으로 영화를 검색한다.
    params = {
        'api_key': '7f4bcebe925d6be694eced873e49d10e',
        'language': 'ko-KR',
        'query': title
    }
    # 제목을 입력하여 결과를 받을것이기 때문에 'query': title를 추가해준다.

    res = requests.get(BASE_URL + path, params).json()
    # BASE_URL + path을 통해 검색할 주소, params을 통해 요청값을 받을 방법을 json 형태로 변환한다.
    results = []
    # 실행 예에 검색 할 수 없는 결과는 빈 리스트로 변환된기 때문에
    # 검색 가능한 결과값들을 모을 리스트를 생성한다.

    if res['results']:
        movie_id = res['results'][0]['id']
        # 3              #1          #2
        # 1 영화 검색에서 받은 결과중 첫번째 영화
        # 2 id 값을 이용하여 추천 영화 목록을 가져올것이다.
        # 3 그렇기 때문에 그 값을 변수로 지정해준다.
        path2 = f'/movie/{movie_id}/recommendations'
        # 활용할 상세 주소를 입력해준다.
        # 이 때 f를 빼먹을시 변수 적용이 안 되어 오류가 발생할 수 있다.
        params2 = {
            'api_key': '7f4bcebe925d6be694eced873e49d10e',
            'language': 'ko-KR',
            'query': movie_id
        }
        # 위에 구한 movie_id 값을 이용해 추천 목록을 받을것이기에 질문에 movie_id 값을 입력해준다.

        res2 = requests.get(BASE_URL + path2, params2).json()
        # path2, param2를 통하여 받은 정보를 json 형태로 변환한다.
        for i in res2['results']:
            # res2의 결과 전체를 반복하며 i 의 값을 지정해준다
            results.append(i['title'])
            # i의 값중 필요한 'tilte' 값만 results라는 비어있는 리스트에 추가해준다.
        return results
        # 'title' 값을 모은 리스트를 반환해준다.
    else:
        return None
        # 이외의 경우 None을 반환한다.


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
