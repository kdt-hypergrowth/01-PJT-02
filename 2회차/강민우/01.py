import requests
from dotenv import load_dotenv
import os


load_dotenv()
api_key = os.getenv('api_key')


def popular_count(): 
    URL ='https://api.themoviedb.org/3/'
    path = 'movie/popular'
    params = {
        'api_key':api_key ,
        'language':'ko-KR'
    }
    response = requests.get(URL+path , params = params).json()
    count = 0
    for a in response.get('results'):
        count += 1
    return count

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
