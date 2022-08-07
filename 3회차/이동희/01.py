import requests as r
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()

def popular_count():
    pass 
    # 여기에 코드를 작성합니다.  
    base_url = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': os.environ.get('api_key'),
        'language': 'ko-KR'
    }
    response = r.get(base_url+path, params=params).json()
    response = response.get('results')
    return len(response)


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
