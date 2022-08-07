import requests
from dotenv import load_dotenv
import os

def popular_count():
    load_dotenv()
    key = os.getenv("80c8b18bf43a69499e913dc21300b23c") 
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
    'api_key': '80c8b18bf43a69499e913dc21300b23c',
    }
    response = requests.get(BASE_URL+path, params=params).json()
    return len(response["results"])

# 아래의 코드는 수정하지 않습니다..
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
