import requests
from pprint import pprint


def ranking():
    api_key = 'a709df78a1a09780128430e580888cb9'
    
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=en-US&page=1'
    response = requests.get(url).json()
    data = response['results']   
    new_list = []       # []는 data가 딕셔너리로 구성된 리스트라서, 그걸 평점순으로 정렬한뒤 새로 담아야하니까 만들었다.
    new_list = sorted(data, key = lambda x : x['vote_average'], reverse = True)[:5] #[-5:][::-1] << 처음엔 이걸썼는데, 알아보니 함수안에 reverse를 쓰면 됐었다. 별 차이 없는것 같다
    # data 딕셔너리를 분류하는데, key를 기준으로 분류한다. 그 키는 'vote_average' 고, 람다함수를 쓰지않으면 data안의 요소는 그냥 딕셔너리라서 정렬을 할수없는데, (키를 불러올수가없다 !!!!) 람다함수로 
    # 해결해야하는 문제였다 

    #1시간 반 이상 붙잡고 있던 문제였는데.. sorted() 함수가 key를 기준으로 정렬가능하다는걸 뒤늦게 알아서 한 줄로 풀리는걸 보고 허탈했다..

    return new_list 
        

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
