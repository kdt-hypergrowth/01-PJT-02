# api : 0adf2f22b2273b1be4feadc7dc662e73
# https://api.themoviedb.org/3/movie/popular?api_key=<<api_key>>&language=en-US&page=1]

# 여기부터 갑자기 어렵게 느껴짐 
# 어떻게 풀어야할지는 알겠는데 설계가 바로 안나옴(문제점)
import requests
from pprint import pprint


def recommendation(title):
    Base_url = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key':'0adf2f22b2273b1be4feadc7dc662e73',
        'language':'ko-KR'
    }


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
