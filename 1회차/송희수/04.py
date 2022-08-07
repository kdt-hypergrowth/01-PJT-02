import requests
from pprint import pprint



def recommendation(title):
    pass 
    # 여기에 코드를 작성합니다. 
    try:
        # 영화 번호 불러오기
        Base_url = 'https://api.themoviedb.org/3'
        path_1 = '/search/movie'
        url_1 = Base_url+path_1
        params_1 = {
            'api_key':'ae8388bc3e6c351e220eb9a018290351',
            'language':'ko-KR',
            'query':title
        }
        movie_id = requests.get(url_1, params = params_1).json().get('results')[0].get('id')

        # 영화 추천목록 가져오기
        url_2 = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations'
        params_2 = {
            'api_key':'ae8388bc3e6c351e220eb9a018290351',
            'language':'ko-KR',
        }
        response = requests.get(url_2, params = params_2).json().get('results')
        lst = []
        for i in response:
            lst.append(i.get('title'))

        return lst

    except:
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
