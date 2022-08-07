import requests
from pprint import pprint


def recommendation(title):
    pass
    
    # ===============
    # movie_id 불러오기
    # ===============

    url = 'https://api.themoviedb.org/3'
    PATH = '/search/movie'
    movie_info = {
    'api_key' : '',
    'language' : 'ko-KR',
    'query' : title
    }

    response = requests.get(url+PATH, params=movie_info).json().get('results')

    # =================================
    # 본격적으로 recommend하는 movie 불러오기
    # =================================

    # 만약 response가 True면
    # (즉, 영화 제목이 검색되어 추천 영화가 나오는 경우 or 제목은 검색이 되나 추천 영화가 반환 안되는 경우)
    if response:
        movie_id = response[0]['id']
        url_1 = 'https://api.themoviedb.org/3'
        PATH_1= f'/movie/{movie_id}/recommendations'
        movie_info_= {
        'api_key' : 'bd811fbe5b564377261911e60b32d7ec',
        'language' : 'ko-KR'
        }

        response_1 = requests.get(url_1+PATH_1, params=movie_info_).json().get('results', None)

        # response1 리스트 안에서 순회하면서 'title'을 리스트에 넣어준다
        movie_r = []
        for mv in response_1:
            movie_r.append(mv['title'])
        
        return movie_r # 반환
    
    # 검색조차 안되는 경우 id값이 없는 경우!
    else:
        return None 



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
