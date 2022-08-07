import requests
from pprint import pprint


def credits(title):
    pass 
    # 여기에 코드를 작성합니다.  

    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    # 영화 제목으로 영화를 검색한다.
    params = {
        'api_key': 'e3ebcaf0cb86336e3fa61579f1f0569b',
        'language': 'ko-KR',
        'query': title
    }
    # 제목을 입력하여 결과를 받을것이기 때문에 'query': title를 추가해준다.

    res = requests.get(BASE_URL + path, params).json()
    # BASE_URL + path을 통해 검색할 주소, params을 통해 요청값을 받을 방법을 json 형태로 변환한다.


    if res['results']:
        movie_id = res['results'][0]['id']
        #3              #1          #2
        #1 영화 검색에서 받은 결과중 첫번째 영화
        #2 id 값을 이용하여 추천 영화 목록을 가져올것이다.
        #3 그렇기 때문에 그 값을 변수로 지정해준다.
        path2 = f'/movie/{movie_id}/credits'
        # 활용할 상세 주소를 입력해준다.
        ## 이 때 f를 빼먹을시 변수 적용이 안 되어 오류가 발생할 수 있다.
        params2 = {
            'api_key': 'e3ebcaf0cb86336e3fa61579f1f0569b',
            'language': 'ko-KR',
            'query': movie_id
        }
        # 위에 구한 movie_id 값을 이용해 추천 목록을 받을것이기에 질문에 movie_id 값을 입력해준다.

        res2 = requests.get(BASE_URL + path2, params2).json()
        # BASE_URL+path2에서 params2의 조건을 바탕으로 출력된 정보를 json 형태로 변환한다.


        # 출력된 값이 cast와 crew를 각 키값으로하고 해당하는 정보들을 리스트형태로 뱔류값을 가지는
        #  딕셔너리 형태이기 때문에 cast와 crew라는 리스트를 만든다.

        cast = []    
        for i in res2["cast"]:
            if i['cast_id'] < 10:
                cast.append(i['name'])
                # res2를 통해 cast_id 값이 10 미만인 인물들의 이름을 cast 폴더에 저장해준다.
        crew = []    
        for j in res2["crew"]:
            if j['department'] == 'Directing' :
                crew.append(j['name'])
                # res2를 통해 department 값이 "Directing"인 인물들의 이름을 crew 폴더에 저장해준다.

        person = {}
        person["cast"] = cast
        person["crew"] = crew
        # cast와 crew를 키값으로 각 리스트들을 설정하여 person이라는 딕셔너리에 넣어준다.


        return person
                # person 딕셔너리를 반환한다.
    else:
        return None
                # 이외 경우 None을 반환한다.

    

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
