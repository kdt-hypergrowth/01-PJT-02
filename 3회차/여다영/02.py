#02. 특정 조건에 맞는 인기 영화 조회

#- 인기 영화 목록 중 평점이 8점 이상인 영화 목록을 출력합니다.
#- requests 라이브러리를 활용하여 TMDB에서 현재 인기 있는 영화 목록(Get Populations) 데이터를 요청합니다.
#- 응답 받은 데이터 중 평점(`vote_average`)이 8점 이상인 영화 목록을 리스트로 반환하는 함수를 작성합니다.

### 결과 예시
#**요청 시점에 따라 다른 결과가 나올 수가 있습니다.**
#[
#    {
#        "adult": false,
#        "backdrop_path": "/odJ4hx6g6vBt4lBWKFD1tI8WS4x.jpg",
#        "genre_ids": [
#            28,
#            18
#        ],
#        "id": 361743,
#        "original_language": "en",
#        "original_title": "Top Gun: Maverick",
#        "overview": "최고의 파일럿이자 전설적인 인물 매버릭은 자신이 졸업한 훈련학교 교관으로 발탁된다. 그의 명성을 모르던 팀원들은 매버릭의 지시를 무시하지만 실전을 방불케 하는 상공 훈련에서 눈으로 봐도 믿기 힘든 전설적인 조종 실력에 모두가 압도된다. 매버릭의 지휘 아래 견고한 팀워크를 쌓아가던 팀원들에게 국경을 뛰어넘는 위험한 임무가 주어지자 매버릭은 자신이 가르친 동료들과 함께 마지막이 될지 모를 하늘 위 비행에 나서는데…",
#        "popularity": 8058.252,
#        "poster_path": "/jMLiTgCo0vXJuwMzZGoNOUPfuj7.jpg",
#        "release_date": "2022-05-24",
#        "title": "탑건: 매버릭",
#        "video": false,
#        "vote_average": 8.4,
#        "vote_count": 1620
#    },
#    {
#        "adult": false,
#        "backdrop_path": "/ocUp7DJBIc8VJgLEw1prcyK1dYv.jpg",
#        "genre_ids": [
#            28,
#            12,
#            878
#        ],
#        "id": 634649,
#        "original_language": "en",
#        "original_title": "Spider-Man: No Way Home",
#        "overview": "미스테리오의 계략으로 세상에 정체가 탄로난 스파이더맨 피터 파커는 하루 아침에 평범한 일상을 잃게 된다. 문제를 해결하기 위해 닥터 스트레인지를 찾아가 도움을 청하지만 뜻하지 않게 멀티버스가 열리면서 각기 다른 차원의 불청객들이 나타난다. 닥터 옥토퍼스를 비롯해 스파이더맨에게 깊은 원한을 가진 숙적들의 강력한 공격에 피터 파커는 사상 최악의 위기를 맞게 되는데…",
#        "popularity": 1513.591,
#        "poster_path": "/voddFVdjUoAtfoZZp2RUmuZILDI.jpg",
#        "release_date": "2021-12-15",
#        "title": "스파이더맨: 노 웨이 홈",
#        "video": false,
#        "vote_average": 8.1,
#        "vote_count": 14255
#    }
#]

#api_key : f4d88a36cfb682b86111c15f97a34324
#https://api.themoviedb.org/3/movie/550?api_key=f4d88a36cfb682b86111c15f97a34324

import requests
from pprint import pprint


def vote_average_movies():
    pass 
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
      'api_key': 'f4d88a36cfb682b86111c15f97a34324'
    }

    response = requests.get(BASE_URL + path, params = params).json()
    results = response.get('results')

    movie_list = []
    for i in range(len(results)):
      if results[i]['vote_average'] >= 8:
        movie_list.append(results[i])

    return movie_list


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
