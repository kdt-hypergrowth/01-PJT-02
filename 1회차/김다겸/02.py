import requests
from pprint import pprint

# 인기 영화 목록 중 평점이 8점 이상인 영화 목록을 출력합니다.
# requests 라이브러리를 활용하여 TMDB에서 현재 인기 있는 영화 목록(Get Populations) 데이터를 요청합니다.
# 응답 받은 데이터 중 평점(`vote_average`)이 8점 이상인 영화 목록을 리스트로 반환하는 함수를 작성합니다.

def vote_average_movies():
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key' : '94ceed584568fa7a9113545f2e4291f5',
        'language' : 'ko-KR'
    }

    # 해당 BASE_URL에서 API request
    response = requests.get(BASE_URL+path, params=params)
    # 요청한 데이터를 json 형태로 가져온 후 'results'에 해당하는 값들을 저장
    movies = response.json().get('results')

    # [{'adult': False, 'backdrop_path': '/393mh1AJ0GYWVD7Hsq5KkFaTAoT.jpg', 'genre_ids': [12, 28, 878],
    # 'id': 507086, 'original_language': 'en',  'original_title': 'Jurassic World Dominion',  'overview': '어쩌구 저쩌구',    
    # 'popularity': 11579.18, 'poster_path': '/odxdUZWZ7fBfy3ZRj063wuJnZvo.jpg', 'release_date': '2022-06-01',
    # 'title': '쥬라기 월드: 도미니언', 'video': False, 'vote_average': 7, 'vote_count': 1794}, ...(생략)]
    
    # 빈 답지 리스트 생성
    answer = []

    # movies에 반복문으로 접근
    for movie in movies:
      # movie의 'vote_average' 값 저장
      vote_average = movie.get('vote_average')
      # 평점이 8 이상이면
      if  vote_average >= 8:
        # answer 리스트에 해당 movie 정보 저장
        answer.append(movie)
    
    return answer


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록중 vote_average가 8 이상인 영화목록 반환
    (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(vote_average_movies())
    """
    [{'adult': False,
      'backdrop_path': '/ocUp7DJBIc8VJgLEw1prcyK1dYv.jpg',
      'genre_ids': [28, 12, 878],
      'id': 634649,
      'original_language': 'en',
      'original_title': 'Spider-Man: No Way Home',
      'overview': '미스테리오의 계략으로 세상에 정체가 탄로난 스파이더맨 피터 파커는 하루 아침에 평범한 일상을 잃게 된다. 문제를 '
                  '해결하기 위해 닥터 스트레인지를 찾아가 도움을 청하지만 뜻하지 않게 멀티버스가 열리면서 각기 다른 차원의 '
                  '불청객들이 나타난다. 닥터 옥토퍼스를 비롯해 스파이더맨에게 깊은 원한을 가진 숙적들의 강력한 공격에 피터 파커는 '
                  '사상 최악의 위기를 맞게 되는데…',
      'popularity': 1842.592,
      'poster_path': '/voddFVdjUoAtfoZZp2RUmuZILDI.jpg',
      'release_date': '2021-12-15',
      'title': '스파이더맨: 노 웨이 홈',
      'video': False,
      'vote_average': 8.1,
      'vote_count': 13954},
    ..생략..,
    }]
    """
