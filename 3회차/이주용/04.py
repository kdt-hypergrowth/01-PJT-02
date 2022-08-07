import requests
from pprint import pprint


def recommendation(title):
    params = {
        'api_key' : '',
        'language' : 'ko-KR',
        'query' : f'{title}'
    }
    base_url = 'https://api.themoviedb.org/3'
    search_url = "/search/movie"
    response = requests.get(base_url + search_url, params=params).json()
    
    # 검색 결과가 존재하지 않을 시 None을 리턴
    if response.get('results') == []:
        return None
    else:
        # 검색 결과의 첫 번째 영화의 id를 추출 후 추천 영화 검색
        movie_id = response.get('results')[0].get('id')
        recommendation_url = f"/movie/{movie_id}/recommendations"
        params_2 = {
            'api_key' : 'a926205337e50c1326d01b6b82f037cd',
            'language' : 'ko-KR'
        }
        movie_list = requests.get(base_url + recommendation_url, params=params_2).json().get('results')
        # movie_list의 제목만 뽑아서 recommendation_list에 넣음
        recommendation_list = []
        for movie in movie_list:
            recommendation_list.append(movie.get('title'))
        return recommendation_list

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
