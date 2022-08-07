import requests
from pprint import pprint


def credits(title):
    
    URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key' : '85bedf36756745d573166cfee3a12aa5',
        'query' : title
    }
    response = requests.get(URL+path, params = params).json()
    if response['results'] == [] :
        return
    # print(response)
    mvid = response['results'][0]['id'] 
    path2 = '/movie/'+str(mvid)+'/credits'
    response2 = requests.get(URL + path2, params = params).json()
    resultdic = {'cast' : [], 'crew' : []}
    for i in response2['cast'] :
        if i['cast_id'] < 10 :
            resultdic['cast'].append(i['name'])
    for j in response2['crew'] :
        if j['department'] == 'Directing' :
            resultdic['crew'].append(j['name'])

    return resultdic
    



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
