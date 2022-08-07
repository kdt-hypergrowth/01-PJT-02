import requests
from pprint import pprint


def recommendation(title):
    pass 
    # 여기에 코드를 작성합니다.  
    BASE_URL = 'https://api.themoviedb.org/3' 
    path = '/search/movie'
    params = {
        'api_key': '6113132e8f47d25f160c7567d23869a3',
        'language': 'ko-KR',
        'query': title
    }
    # 결과는 제목 입력해서 받음
    res = requests.get(BASE_URL + path, params).json()
    results = []

    if res['results']:
        movie_id = res['results'][0]['id']
        # 첫번째 영화
        # id 값으로 영화 목록 
        path2 = f'/movie/{movie_id}/recommendations'
        params2 = {
        'api_key': '6113132e8f47d25f160c7567d23869a3',
        'language': 'ko-KR',
        'query': movie_id
    }

        res2 = requests.get(BASE_URL + path2, params2).json()
        for i in res2['results']:
            # res2 반복해서 i값 할당
            results.append(i['title'])
            # 리스트에 추가
        return results
    else:
        return None
        # 아니면 None 
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
