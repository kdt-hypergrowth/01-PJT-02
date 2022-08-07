# 문제03. 특정 조건에 맞는 인기 영화 조회
# Getpopulations 데이터 요청 및 평점(vote_average)이 높은 영화 5개의 정보를 리스트로 반환

import requests
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('api_key')


def ranking():
    pass 
    # 여기에 코드를 작성합니다.
    # 변수 선언 및 접속 URL 설정
    URL = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=ko'

    # 요청 보내서 응답을 받음
    response = requests.get(URL)

    # 응답 받은 데이터(json) 내 영화정보가 담긴 json 파일을 가져옴
    data = response.json()

    # 영화 정보를 담을 리스트 선언
    movie_list = []
    movie_list_sort = []

    # 평점 정보를 가져와서 sorted() 함수 역정렬
    for i in range(0, len(data.get('results'))):
      movie_list.append(data.get('results')[i])
      movie_list_sort = sorted(data.get('results'), key=lambda k:k['vote_average'], reverse=True)

    # vote_average 점수 기준 역정렬된 리스트 요소 중 5개만 반환
      return movie_list_sort[0:5]

    
      
#    return movie_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록을 정렬하여 평점순으로 5개 영화 반환
    (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(ranking())
    """
    [{'adult': False,
      'backdrop_path': '/odJ4hx6g6vBt4lBWKFD1tI8WS4x.jpg',
      'genre_ids': [28, 18],
      'id': 361743,
      'original_language': 'en',
      'original_title': 'Top Gun: Maverick',
      'overview': '최고의 파일럿이자 전설적인 인물 매버릭은 자신이 졸업한 훈련학교 교관으로 발탁된다. 그의 명성을 모르던 팀원들은 '
                  '매버릭의 지시를 무시하지만 실전을 방불케 하는 상공 훈련에서 눈으로 봐도 믿기 힘든 전설적인 조종 실력에 모두가 '
                  '압도된다. 매버릭의 지휘 아래 견고한 팀워크를 쌓아가던 팀원들에게 국경을 뛰어넘는 위험한 임무가 주어지자 매버릭은 '
                  '자신이 가르친 동료들과 함께 마지막이 될지 모를 하늘 위 비행에 나서는데…',
      'popularity': 911.817,
      'poster_path': '/jMLiTgCo0vXJuwMzZGoNOUPfuj7.jpg',
      'release_date': '2022-06-22',
      'title': '탑건: 매버릭',
      'video': False,
      'vote_average': 8.4,
      'vote_count': 1463},
    ..생략..,
    }]
    """
