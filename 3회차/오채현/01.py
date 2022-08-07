#인기 영화 목록의 개수 출력
from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_KEY = os.environ.get('TMDB_API_KEY')

Base_Url = 'https://api.themoviedb.org/3'

path = '/movie/popular'

params = {
    'api_key': API_KEY,
    'language': 'ko-KR'
}



def popular_count():
    pass 
    # 여기에 코드를 작성합니다. 
    res = requests.get(Base_Url+path, params=params).json()
    data = res['results']
    

    return  len(data)



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
