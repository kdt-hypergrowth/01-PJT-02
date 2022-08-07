import requests
from pprint import pprint
from dotenv import load_dotenv
import os


load_dotenv()
APIKEY = os.getenv('APIKEY')   # 환경변수 설정 및 가져오기
# 같은 방법
# APIKEY = os.environ.get('APIKEY')

# base_url = 'https://api.themoviedb.org/3'
# path = '/movie/popular'
# params = {
#     'api-key': APIKEY,
#     'language': 'ko-KR'
# }

def popular_count():
    # 유효하지 않은 API key라고 뜸
    # response = requests.get(base_url + path, params = params).json()
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={APIKEY}&language=ko-KR"
    response = requests.get(url).json()
    movie_list = response["results"]
    # print(res)
    return len(movie_list)

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
