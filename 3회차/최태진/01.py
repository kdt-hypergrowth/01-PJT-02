#인기 영화 조회
#KeyError: 'result' result 키 없음 -> results임 dict으로 키접근 시, 단어 잘 볼것
#7506ce2e3f3a4cad52958b2c8f243e2e
#https://api.themoviedb.org/3/movie/76341?api_key=<<api_key>>


import requests
from pprint import pprint 
def popular_count():
    base_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key' : '7506ce2e3f3a4cad52958b2c8f243e2e'

    }
    response = requests.get(base_URL+path, params=params).json()
   
    # response 내 results 키를 data변수로 치환
    data = response.get('results')
    #리스트 내 딕셔너리 사용
    #list_name[i]['key']
    print(len(data))
    return len(data)

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    pprint(popular_count())
    # 20
