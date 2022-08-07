import requests
from pprint import pprint


def vote_average_movies():
    api_key = 'a709df78a1a09780128430e580888cb9'
    
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=en-US&page=1'
    response = requests.get(url).json()
    data = response['results']   #위의 url에 들어가보니 리스트 딕셔너리로 중첩된 코드가 있길래, 그걸 이용했다.
    new_list = []     # 평점 8 이상의 영화들을 따로 뽑기위해서 미리 빈 리스트를 만든다
    for i in data:    # data는 인기영화 1페이지의 20개 영화정보를 리스트로 큰 틀을 만든뒤 딕셔너리로 정리한 코드??다. 그래서 리스트의 요소들을 (영화 각각의 정보가 담긴 딕셔너리들을) 순회하기위해 for문 작성
        if i['vote_average'] >= 8:  # i는 data의 각각의 요소, 즉 영화 한개의 정보를 담고있는 딕셔너리이므로, 그 딕셔너리에서 vote_average라는 키의 값이 8이상인 경우,
            new_list.append(i)           # 빈 리스트인 new_list에 추가한다. 
    return new_list     # 함수는 그 리스트를 반환한다.


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
