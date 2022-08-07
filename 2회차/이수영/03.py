import requests
from pprint import pprint
BASE_URL = 'https://api.themoviedb.org/3'
path = '/movie/popular'

params = {
    'api_key': 'dcc1e7ed069f7427a2816e92b32e7c8b',
    'language': 'ko-KR'
}

response = requests.get(BASE_URL+path, params = params).json()

def ranking():
  top5 = [] # 상위 5개의 영화 가 들어갈 리스트 작성
  movies = response.get('results')
  sor_movies = sorted(movies, key = lambda x: x['vote_average'], reverse = True)
  # movies 안에 있는 영화 정보는 딕셔너리이기 때문에 딕셔너리 각각의 평점을 정렬
  # 해야 한다. 그러기 위해서는 람다함수를 사용하여 sorted 함수의 키를 정하고 실행
  # 한다. 마지막 리버스를 돌려서 높은 순서가 먼저 나오게 한다.
  top5 = sor_movies[:5] # 0, 1, 2 ,3 , 4 까지 순서대로 출력
  return top5

  
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
