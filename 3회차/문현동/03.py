import os
import requests
from pprint import pprint
from dotenv import load_dotenv



def ranking():
  
    load_dotenv(verbose = True)
    api_key = os.getenv('api_key')
    base_url = os.getenv('base_url')
    population_path = "/movie/popular"
    
    payload =\
    {
      "api_key" : api_key,
      "language" : "ko-KR"
    }
    
    
    
    response = requests.get(url = base_url + population_path, params = payload).json()
        
    sorted_movie_info_list = []
    
    for movie_info in response.get("results"):
      print(movie_info.get("vote_average"))
      
      sorted_movie_info_list = sorted(response.get("results"), key = lambda movie_info : movie_info["vote_average"], reverse = True)
      # 위 코드를 한글로 번역하면 이렇다.
      # 정렬된 리스트 = 정렬값을 반환 (리스트 전체에 대해서, 키는 람다함수의 반환값이고 람다함수는 영화정보를 인자로 받았을 때 그 영화정보의 평점을 값으로 가짐, 내림차순 = 참)
      # 즉 영화정보의 평점을 값으로 가지는 키를 기준으로 내림차순 정렬을 한다.
    
    return sorted_movie_info_list[:5]


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
