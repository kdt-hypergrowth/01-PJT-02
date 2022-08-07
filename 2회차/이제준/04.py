import requests
from pprint import pprint

def recommendation(title):
    base_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'

    params = {
        'api_key' : '652241f716c0f8b8f5006465a644f600',
        'language': 'ko-KR',
        'query': f'{title}'      
        # query가 필수이고, title을 넣으면 영화 제목을 검색할 수 있다
        # recommendation(title) 함수를 만든 후 괄호 안에 영화 제목을 입력하면 된다
    }
    
    # 마지막에 .get('results')라고 하는 것은, response 자체가 현재 List이기 때문이다
    # List에 있는 dict 중 'result' dictionary를 가져오는 것
    response = requests.get(base_URL + path, params = params).json().get('results')

    # response에 아무것도 없으면 None을 반환한다
    if len(response) == 0:
        return None
    # response는 리스트, 첫번째 리스트 element 중 'id'라는 key의 value를 가져온다
    else:
        id = response[0]['id']

    # f-string을 안 쓰면 위에서 찾은 id와 연결이 안 된다
    path = f'/movie/{id}/recommendations'

    response = requests.get(base_URL + path, params = params).json().get('results')

    result = []
    for i in response:
        result.append(i['title'])

    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
#     """
#     제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
#     추천 영화가 없을 경우 []를 반환
#     영화 id 검색에 실패할 경우 None을 반환
#     (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
#     """
    pprint(recommendation('기생충'))
#     # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
#     # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
