import requests
from pprint import pprint


def recommendation(title):
    # 여기에 코드를 작성합니다.  
    base_url = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': 'e2be94a1762b4b81af8b205d5e2bcb5f',
        'language': 'ko-KR',
        'query': title
    }
    response = requests.get(base_url+path, params=params).json()
    if len(response['results']) < 1:
        return None
    mv_id = response['results'][0]['id']

    base_url_2 = 'https://api.themoviedb.org/3'
    path_2 = f'/movie/{mv_id}/recommendations'
    params_2 = {
        'api_key': 'e2be94a1762b4b81af8b205d5e2bcb5f',
        'language': 'ko-KR'
    }
    response_2 = requests.get(base_url_2+path_2, params=params_2).json()
    results_2 = response_2['results']
    title_lst = []
    for i in range(len(results_2)):
        title_lst.append(results_2[i]['title'])
    return title_lst


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
