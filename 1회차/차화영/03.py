import requests
from pprint import pprint
from dotenv import load_dotenv
import os

def ranking():
    load_dotenv()
    key = os.getenv('80c8b18bf43a69499e913dc21300b23c')
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
    'api_key': '80c8b18bf43a69499e913dc21300b23c',
    'language': 'ko-KR'
    }
    response = requests.get(BASE_URL+path, params=params).json()
    results = response.get('results')
    movies = sorted(results, key=lambda results : results['vote_average'],  reverse=True)[:5]
    # list.sort()와 sorted()는 모두 비교하기 전에 각 리스트 요소에 대해 호출할 함수(또는 다른 콜러블)를 지정하는 key 매개 변수를 가지고 있다.
    # key 매개 변수의 값은 단일 인자를 취하고 정렬 목적으로 사용할 키를 반환하는 함수 -- 객체의 인덱스 중 일부를 키로 사용하여 복잡한 객체를 정렬하는 것
    # sorted()는 불리언 값(True, False)을 갖는 reverse 매개 변수를 받아들인다. --- sorted의 기본값이 오름차순이므로 reverse = True로 내림차순 정렬한다.
    # 평점 상위 5개만 출력 위해 리스트 슬라이싱[:5]
    return movies

# 아래의 코드는 수정하지 않습니다..
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
