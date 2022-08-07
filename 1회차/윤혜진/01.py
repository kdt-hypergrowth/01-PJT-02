import requests
from pprint import pprint
from dotenv import load_dotenv
import os

def popular_count():
    load_dotenv()
    key = os.environ.get('TMDB_API_key')

    base_url = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    prameters = {
        'api_key' : key,
        'language': 'ko-KR',
        'page':1
    }
   
    response = requests.get(base_url + path, params=prameters).json()
    # pprint(response.json())
    popular_movies_info = response.get('results')
    return len(popular_movies_info)

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
