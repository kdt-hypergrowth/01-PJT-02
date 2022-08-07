 # dcc1e7ed069f7427a2816e92b32e7c8b 마이 API 키
import requests
BASE_URL = 'https://api.themoviedb.org/3'   # 필요 URL 불러오기
path = '/movie/popular'                      # 필요한 정보의 불러오기

params = {
    'api_key': 'dcc1e7ed069f7427a2816e92b32e7c8b',    # API 키 입력
    'language': 'ko-KR'
}

response = requests.get(BASE_URL+path, params = params).json()
def popular_count():
    movies = response.get('results')     # URL에서 가져온 리스폰스를 Movies 라는 리스트로 생성
    return len(movies)                   # 생성된 리스트 안에 movie 정보 딕셔너리의 객체의 개수
   
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
