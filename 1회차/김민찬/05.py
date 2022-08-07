import requests
from pprint import pprint

def credits(title):
    pass 
    # 여기에 코드를 작성합니다.  

    params = {
        "api_key": '8854669b886a6c07c12ea947bcc2311d',
        'language': 'ko-KR'
    }

    result_dict = {'cast':[], 'crew':[]}

    BaseURL = "https://api.themoviedb.org/3"
    path = "/movie/496243/credits"
    response = requests.get(BaseURL + path, params = params).json()

    if 'success' in response.keys():
        return None

    for actor in response['cast']:

        if actor['cast_id'] < 10:
            result_dict['cast'].append(actor['name'])

    for crew in response['crew']:

        if crew['department'] == 'Directing':
            result_dict['crew'].append(crew['name'])

    return result_dict

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