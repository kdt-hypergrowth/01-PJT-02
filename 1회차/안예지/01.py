import os
from dotenv import load_dotenv
import requests


load_dotenv()

# 인기 영화 목록의 개수 출력
# 현재 인기 있는 영화 목록(Get Populations)에 데이터를 요청

def popular_count():
    
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': os.getenv('TMDB'),
        'language' : 'ko-KR'        
    }
    
    response = requests.get(BASE_URL+path, params=params).json()
    
    cnt = 0
    for n in response['results']:
        n.get('id')
        cnt += 1
    
    return cnt

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20