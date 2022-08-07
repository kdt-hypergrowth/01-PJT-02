import requests
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)
key = os.getenv('key')
def popular_count():
    base = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
    'api_key': key,
    'language': 'ko-KR'
    }

    response = requests.get(base+path, params=params).json()
    return len(response.get('results'))

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
