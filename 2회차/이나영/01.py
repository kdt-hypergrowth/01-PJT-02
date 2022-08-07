from unittest import result
import requests
#BASE_URL로 요청을 보내서 응답(response)받은 것을 가져와.

def popular_count():
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
    'api_key': '1a34d0a469973ec909fc02914699f88d',
    'language': 'ko-KR'
    }
    response = requests.get(BASE_URL+path, params=params).json()   

#BASE_URL로 요청을 보내서 응답(response)받은 것을 가져와.
    
    cnt = 0
    for i in response.get('results'):
        cnt+= 1
    return cnt
    
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
