import requests # requests 불러오기
from pprint import pprint # pprint 불러오기


def ranking(): 
  BASE_URL = 'https://api.themoviedb.org/3' # api 주소..!
  path = '/movie/popular' # 세부 주소
  params = {
    'api_key' : '801b2f9c7a6d8dce6f3bd7f807c9ffc5', # 세부 정보 
    'language' : 'ko-KR'
  }
  
  response = requests.get(BASE_URL+path, params=params).json() # requests 정보 가져오기
  movie_list = response.get('results')  # movie_list에 requests 가져온 정보(results) 저장하기!
  # 평점순으로 만들고 range 사용해서 5개까지 반환하면 끝
  # movie에 sorted 정렬(movie_list를 , key=lambda 람다로 x:x x를 기준으로'vote_averge'를! reverse=True 이용해서 내림차순 정렬)
  movie = sorted(movie_list, key=lambda x:x['vote_average'], reverse = True)
  
  
  return movie[:5] # 나오는 리스트 중에 5개까지만 출력!
  
  
  
  
  # top5 = []

  # movies = sorted(movie_list, key=lambda x: x['vote_average'], reverse=True)
  # top5 = movies[:5]
  # return top5
  # print(result)
    
    


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
