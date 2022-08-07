import requests
from pprint import pprint


def credits(movie_name):
    pass
    base_url = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
    'api_key': '0f810078345847f7d4b6930619626f55', #API값 정의
    'language': 'ko-KR',
    'query': movie_name #영화 이름으로 찾을꺼야
    }
    response = requests.get(base_url + path, params = params).json()
    
    if response['results']:
        movie_id = response['results'][0]['id']
        path = f'/movie/{movie_id}/credits'

        params = {
            'api_key': '0f810078345847f7d4b6930619626f55',
            'language': 'ko-KR',
            'movie_id': movie_id #영화id로 찾을꺼야
        }
        res = requests.get(base_url + path, params).json()
        pprint(res)
        #  딕셔너리 값을 cast와 crew라는 리스트를 만들어 출력.
        cast = []    
        for i in res["cast"]:
            if i['cast_id'] < 10:
                cast.append(i['name'])
                # res를 통해 cast_id 값이 10 미만인 인물들의 이름을 cast리스트에 저장
        crew = []    
        for j in res["crew"]:
            if j['department'] == 'Directing' :
                crew.append(j['name'])
                # res를 통해 department 값이 "Directing"인 인물들의 이름을 crew리스트에 저장

        person = {}
        person["cast"] = cast
        person["crew"] = crew
        # cast와 crew를 키값으로 각 리스트들을 설정하여 person이라는 딕셔너리에 넣어준다.


        return person
                # person 딕셔너리를 반환한다.
    else:
        return None
                # 이외 경우 None을 반환한다.


    # 여기에 코드를 작성합니다.  


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
