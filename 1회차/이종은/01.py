

#54a9fff1e7fa56a1b0a2cc7c70c99ac4
#https://api.themoviedb.org/3/movie/76341?api_key=<<api_key>>

import requests
from pprint import pprint

def popular_count():
    base_url = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
    'api_key' : '54a9fff1e7fa56a1b0a2cc7c70c99ac4', 
    'language' : 'ko-KR'
    }
    response = requests.get(base_url+path, params=params).json() #응답 받은 값을 가져온다 
    # cnt = 0
    # # for i in response.get('results'):
    # #     cnt += 1
    # #     if i == "":
    # #         break
    popular_count = len(response.get('results')) #결과 값 딕셔너리 키 값의 리스트 내 갯수가 몇개인지 확인
    return popular_count #인기 리스트 영화 갯수 함수 리턴
    



#아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
