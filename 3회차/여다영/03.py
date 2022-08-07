#03. 특정 조건에 맞는 인기 영화 조회

#- 인기 영화 목록을 평점이 높은 순으로 5개를 정렬하여 영화 데이터 목록을 출력합니다.
#- requests 라이브러리를 활용하여 TMDB에서 현재 인기 있는 영화 목록(Get Populations) 데이터를 요청합니다.
#- 응답 받은 데이터 중 평점(`vote_average`)이 높은 영화 5개의 정보를 리스트로 반환하는 함수를 작성합니다.

#**TIP.** 정렬시 sorted 함수의 key를 활용합니다.

#sorted( <list> , key = <function> , reverse = <bool>)
#<list> 뿐 아니라, <Tuple>, <Dictionary>, <Str>에도 사용 가능하다.

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
#	   // ... 생략
#    {
#        "adult": false,
#        "backdrop_path": "/wNQpfAZkySbinb93qVwWIWaot1x.jpg",
#        "genre_ids": [
#            10402,
#            14,
#            35,
#            878,
#            10751,
#            10770
#        ],
#        "id": 809107,
#        "original_language": "en",
#        "original_title": "Z-O-M-B-I-E-S 3",
#        "overview": "올해는 제드와 애디슨에게 시브룩에서의 마지막 해이고, 시브룩은 몬스터와 인간에게 천국이 되었다. 제드는 좀비 최초로 대학에 입학하고자 풋볼 장학생이 되려고 애쓰고, 애디슨은 전국 응원 대회를 준비 중이다. 은하계 외부인들이 나타나 응원 대회에 출전하게 되자, 시브룩에서는 이들이 대회 출전보다 다른 속셈이 있을지도 모른다는 의심이 커져 간다.",
#        "popularity": 1848.58,
#        "poster_path": "/egX5gH8UmRl2eLL4EMbJfm5p05d.jpg",
#        "release_date": "2022-07-09",
#        "title": "좀비스 3",
#        "video": false,
#        "vote_average": 7.9,
#        "vote_count": 86
#    }
#]

#api_key : f4d88a36cfb682b86111c15f97a34324
#https://api.themoviedb.org/3/movie/550?api_key=f4d88a36cfb682b86111c15f97a34324

import requests
from pprint import pprint


def ranking():
    pass 
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
      'api_key' : 'f4d88a36cfb682b86111c15f97a34324'
    }

    response = requests.get(BASE_URL + path, params = params).json()
    results = response.get('results')

    rank = sorted(results, key = lambda x : -x['vote_average'])

    top_five = []
    for i in range(5):
      top_five.append(rank[i])

    return top_five


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
