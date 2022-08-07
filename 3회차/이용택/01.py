import requests
from pprint import pprint
from dotenv import load_dotenv
import os


def popular_count():
    load_dotenv()
    key = os.getenv("KEY")
    base_url = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': key,
        'language': 'ko-kr'
    }

    res = requests.get(base_url + path, params = params)
    popular_movie = res.json()['results']
    result = len(popular_movie)

    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
