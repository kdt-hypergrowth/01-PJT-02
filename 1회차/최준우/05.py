import requests
from pprint import pprint


def credits(title):
    pass 
    # 여기에 코드를 작성합니다.  
    SEARCH_URL = f'https://api.themoviedb.org/3/search/movie?api_key=2493cbf091c3129450beca0dc74b2470&language=ko-KR&query={title}&page=1&include_adult=true'
    response_search = requests.get(SEARCH_URL).json()
    movie_id = ''

    for i in range(0, len(response_search.get('results'))):
        if response_search.get('results')[i].get('title') == title:
            movie_id = response_search.get('results')[i].get('id')
    
    BASE_URL = 'https://api.themoviedb.org/3'
    path = f'/movie/{movie_id}/credits'
    params = {
        'api_key' : '2493cbf091c3129450beca0dc74b2470',
        'language' : 'ko-KR'
    }

    response = requests.get(BASE_URL + path, params = params).json()
    
    credits_list = {}
    cast_list = []
    crew_list = []

    if (movie_id == ''):
        return None
    else:
        for i in range(0,len(response.get('cast'))):
            if response.get('cast')[i].get('cast_id') < 10:
                cast_list.append(response.get('cast')[i].get('name'))
        for i in range(0,len(response.get('crew'))):
            if response.get('crew')[i].get('department') == 'Directing':
                crew_list.append(response.get('crew')[i].get('name'))
        
        credits_list['cast'] = cast_list
        credits_list['crew'] = crew_list

        return credits_list

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
