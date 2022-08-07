import requests
from pprint import pprint


def credits(title):
    pass 
    # 여기에 코드를 작성합니다.  
    Base_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params={
        'api_key':'9e7ad8abf0f44312c8921229635fe29f',
        'language':'ko-KR',
        'query': title }
    response = requests.get(Base_URL+path, params=params).json().get('results')

    if not response: # response가 비어있으면 none 반환
        return None
    movie_id = response[0].get('id')
    path_1=f'/movie/{movie_id}/credits' # recommenadation을 위한 API GET에 해당하고 {}를 통해 바뀌는 값을 넣어준다.
    response1=requests.get(Base_URL + path_1, params=params).json()

    dic={}
    cast=[]
    crew=[]

    for i in response1.get('cast'):
        if i.get('cast_id')<10:
            cast.append(i.get('name'))
    dic['cast']=cast

    for i in response1.get('crew'):
        if i.get('department') =='Directing':
            crew.append(i.get('name'))
    dic['crew']=crew

    if dic =={}:
        return []
    else:
        return dic



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
