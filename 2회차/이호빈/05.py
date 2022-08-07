from distutils.file_util import move_file
import requests
from pprint import pprint


def credits(title):
    url = 'https://api.themoviedb.org/3/'
    path = 'search/movie'
    params = {
        'api_key': '57289526949f876f1e243aee06612c5f',
        'language': 'ko-KR',
        'query' : f"{title}"
    }
    # 최종적으로 조건에 부합하는 연출진과 출연진의 정보를 빈 딕셔너리에 저장한다.
    member_info = {"crew" : [], "cast" : []}

    response = requests.get(url + path, params = params).json()
    if response.get('results') == []:
        return None
    else:
        # 첫 번째 영화의 id
        result_id = response.get('results')[0].get('id')

        # 출연진이랑 연출진 찾기
        c_url = f"/movie/{result_id}/credits"
        credits_response = requests.get(url + c_url, params = params).json()

        for crew in credits_response.get('crew'):
            if crew.get('department') == "Directing":
                member_info['crew'].append(crew.get('name'))


        for cast in credits_response.get('cast'):
            if cast.get('cast_id') < 10:
                member_info['cast'].append(cast.get('name'))


    return member_info
                
                
        



    


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
