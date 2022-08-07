# 문제01. 인기 영화 조회
# Getpopulations 데이터 요청 및 영화 개수 반환 함수 작성

# requests 모듈을 가져옴
import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('api_key')


def popular_count():
    pass 
    # 여기에 코드를 작성합니다.
    # 변수 선언 및 접속 URL 설정
    URL = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=ko'

    # 요청 보내서 응답을 받음
    response = requests.get(URL)

    # 응답 받은 데이터(json) 내 영화정보가 담긴 json 파일을 가져옴
    data = response.json()

    # json 파일 내 딕셔너리로 정의된 results 키의 리스트 갯수를 구함
    movies = len(data.get('results'))

    # 리스트 갯수를 반환
    return movies

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
