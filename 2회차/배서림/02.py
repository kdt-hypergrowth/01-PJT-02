# 02. 특정 조건에 맞는 인기 영화 조회

# 인기 영화 목록 중 평점이 8점 이상인 영화 목록을 출력합니다.
# requests 라이브러리를 활용하여 TMDB에서 현재 인기 있는 영화 목록(Get Populations) 데이터를 요청합니다.
# 응답 받은 데이터 중 평점(`vote_average`)이 8점 이상인 영화 목록을 리스트로 반환하는 함수를 작성합니다.


import requests
from pprint import pprint

def vote_average_movies():
    URL = 'https://api.themoviedb.org/3/movie/popular'
    params = {
        'api_key': '64960f74c1f585f363c60f7fa0745d1f',
    }

    response = requests.get(URL, params=params).json() # page, results, total_results, total_pages
    lst = response.get('results') # results 내의 objects
    
    # 생각한 접근법
    # 영화 정보 값은 딕셔너리들이 모인 리스트로 이루어져 있음
    # 리스트 내의 > 딕셔너리 내의 > 키를 통해 평점을 알아내야 함
    # 리스트를 인덱스로 접근하면 특정 딕셔너리에 바로 갈 수 있음
    # '인덱스를 통해 접근한 리스트'를 변수로 지정하고 / .get을 이용해 평점을 따로 얻을 수 있음
    # 그렇게 얻은 값 >= 8.0 이면 반환하도록 함

    # 인덱스에 들어갈 숫자는 0~19 니까 이걸 반복시켜야 함

    num = 0
    twenty = int(len(lst))
    while True:
        if num < twenty:
            dct = lst[int(num)]
            avg = dct.get('vote_average')
            if avg > 7.9:
                return dct
            else:
                num += 1


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
