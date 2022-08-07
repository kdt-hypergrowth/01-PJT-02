import requests
from dotenv import load_dotenv
import os
load_dotenv()

def popular_count():
    URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': os.environ.get('api_key'),
        'language': 'ko-KR'
    }
    response = requests.get(URL+path, params=params).json()
    movie = response.get('results')
    cnt = 0
    for i in movie:
        cnt += 1    
    return(cnt)


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
