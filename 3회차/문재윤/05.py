import requests
from pprint import pprint


def credits(title):
    pass 
    # 여기에 코드를 작성합니다.  
    base_url = 'https://api.themoviedb.org/3/search/movie'
    params = {'api_key' : '6536d1c9342b7cc9209b1ef937331746',
    'language' : 'ko-KR',
    'query'  : title}
    response = requests.get(base_url, params = params).json().get('results')
    response = response[0]
    response = response.get('id')
    print(response)
    movie_id = response

    base_url2 = f'https://api.themoviedb.org/3/movie/{movie_id}/credits'
    params2 = {'api_key' : '6536d1c9342b7cc9209b1ef937331746',
    'language' : 'ko-KR',}

    response1 = requests.get(base_url2, params = params2)
    response2 = response1.json().get('cast')

    cast1 = []
    crew2 = []
    for i in response2:
        if i.get('cast_id') < 10:
            cast1.append(i.get('name'))
           
    

    response3 = response1.json().get('crew')
    for e in response3:
        if e.get('department') == 'Directing':
            crew2.append(i.get('name'))

    
    return {"cast": cast1, "crew": crew2}
   
            
   
    


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
