import requests
from pprint import pprint


def recommendation(title):

    search_url = 'https://api.themoviedb.org/3/search/movie'
    search_params = {
            'api_key' : '09a613146a968647b2f3039070613000',
            'language' : 'ko',
            'query' : title,
            'page' : 1,
            'include_adult' : 'false'
        }

    search_response = requests.get(search_url, params=search_params)
    search_results = search_response.json()['results']

    search_id = []

    try :
        for i in search_results :
            search_id.append(i['id'])
        movie_id = search_id[0]
    
    except IndexError :
        return None

    recomm_url = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations'
    recomm_params = {
            'api_key' : '09a613146a968647b2f3039070613000',
            'language' : 'ko',
            'page' : 1
        }

    recomm_response = requests.get(recomm_url, params=recomm_params)
    recomm_results = recomm_response.json()['results']

    recomm_list = []

    for i in recomm_results :
        recomm_list.append(i['title'])
        
    return recomm_list



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
