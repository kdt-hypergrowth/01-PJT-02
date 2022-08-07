import requests
from pprint import pprint


def vote_average_movies():
  
  BASE_URL = 'https://api.themoviedb.org/3' # api 불러 올 주소! 
  path = '/movie/popular' # 세부 주소! 
  params = {
    'api_key' : '801b2f9c7a6d8dce6f3bd7f807c9ffc5', # 세부 정보! 
    'language' : 'ko-KR'
  }
  
  response = requests.get(BASE_URL+path, params=params).json() # requests 받아오기! = 정보 불러오기!
  movie_list = response.get('results') # movie_list에 requests 받아 온 results 저장!
  
  result = [] # result 라는 빈 리스트 만들기!
  for i in movie_list: # 반복문 사용해서 i에 데이터 저장하기!
    if i.get('vote_average') >= 8.0: # 만약 if i.get i에서 가져온 vote_averge 가 >= 8점 이상일 때
      result.append(i) # result에 목록 append(i의 정보를) ! 

  return result # result 라는 8.0점 이상의 영화를 저장한 저장소를 반환
    

      


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # """
    # popular 영화목록중 vote_average가 8 이상인 영화목록 반환
    # (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    # """
    pprint(vote_average_movies())
    # """
    # [{'adult': False,
    #   'backdrop_path': '/ocUp7DJBIc8VJgLEw1prcyK1dYv.jpg',
    #   'genre_ids': [28, 12, 878],
    #   'id': 634649,
    #   'original_language': 'en',
    #   'original_title': 'Spider-Man: No Way Home',
    #   'overview': '미스테리오의 계략으로 세상에 정체가 탄로난 스파이더맨 피터 파커는 하루 아침에 평범한 일상을 잃게 된다. 문제를 '
    #               '해결하기 위해 닥터 스트레인지를 찾아가 도움을 청하지만 뜻하지 않게 멀티버스가 열리면서 각기 다른 차원의 '
    #               '불청객들이 나타난다. 닥터 옥토퍼스를 비롯해 스파이더맨에게 깊은 원한을 가진 숙적들의 강력한 공격에 피터 파커는 '
    #               '사상 최악의 위기를 맞게 되는데…',
    #   'popularity': 1842.592,
    #   'poster_path': '/voddFVdjUoAtfoZZp2RUmuZILDI.jpg',
    #   'release_date': '2021-12-15',
    #   'title': '스파이더맨: 노 웨이 홈',
    #   'video': False,
    #   'vote_average': 8.1,
    #   'vote_count': 13954},
    # ..생략..,
    # }]
    # """
