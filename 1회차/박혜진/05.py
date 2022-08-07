import requests
from pprint import pprint


def credits(title):

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


    cre_url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits'
    cre_params = {
            'api_key' : '09a613146a968647b2f3039070613000',
            'language' : 'ko',
        }

    cre_response = requests.get(cre_url, params=cre_params)
    cre_results = cre_response.json()

    actor_dict = {'cast' : [], 'crew' : []}

    if 'status_code' in cre_results.keys() :
        return None

    for a in cre_results['cast'] :
        if a['cast_id'] < 10 :
            actor_dict['cast'].append(a['name'])


    for c in cre_results['crew'] :
        if c['department'] == 'Directing' :
            actor_dict['crew'].append(c['name'])

    
    return actor_dict



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
