import requests
from pprint import pprint


def credits(title):
    base_url = 'https://api.themoviedb.org/3/'
    path = f'search/movie?query={title}'
    params = {
        'api_key' : '09d0041de8747ddc735a2981381ae949',
        'language' : 'ko',
    }
    res = requests.get(base_url+path, params=params)
    data = res.json()

    #새 id를 가지고 data를 다시 가져오기 시작
    try:
        idResult = data['results'][0]['id']
        path = f'movie/{idResult}/credits'
        res = requests.get(base_url+path, params=params)
        data = res.json()
        castList = []
        crewList = []
        castAndCrew={}
        
        for i in data['cast']:
            if i['cast_id'] < 10 :
                castList.append(i['original_name'])

        for i in data['crew']:
            if i['department'] == 'Directing'  :
                crewList.append(i['original_name'])

        castAndCrew["cast"] = castList
        castAndCrew["crew"] = crewList
        return castAndCrew
        # dataList = []
    #     for i in data['results']:
    #         dataList.append(i['title'])
    #     return dataList
    except IndexError:
        return None 


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
