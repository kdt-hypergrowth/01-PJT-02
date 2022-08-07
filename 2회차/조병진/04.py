# 04. 영화 조회 및 추천 영화 조회
# - 영화 제목으로 검색을 하여 추천 영화 목록을 출력합니다.
# requests 라이브러리를 활용하여 TMDB에서 영화제목으로 영화를 검색(Search Movies)합니다.
# 응답 받은 결과 중 첫번째 영화의 id 값을 활용하여 TMDB에서 추천 영화 목록(Get Recommendations)을 가져옵니다.
# 추천 영화 목록을 리스트로 반환하는 함수를 작성합니다.

import requests
from pprint import pprint


def recommendation(title):
    pass

    url = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    URL = url + path
    params = {
        'api_key': '837e86c41f738f95ed4b63bd28dabae4',
        'language': 'ko-KR',
        # 검색한 영화값
        'query': title
    }

    response = requests.get(
        URL, params=params).json().get('results')

    # 만일 검색한 영화가 없다면
    if len(response) == 0:
        # 값은 None
        return None

    url2 = 'https://api.themoviedb.org/3'
    # 검색한 영화의 id 값으로 주소 입력
    path2 = '/movie/'+str(response[0].get('id'))+'/recommendations'
    URL2 = url2 + path2
    params = {
        'api_key': '837e86c41f738f95ed4b63bd28dabae4',
        'language': 'ko-KR',
    }

    # 추천 영화 제목을 넣을 박스
    result = []
    response2 = requests.get(URL2, params=params).json().get('results')

    for i in response2:
        result.append(i.get('title'))

    return result


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
