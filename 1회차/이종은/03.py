import requests
from pprint import pprint


def ranking():
  base_url = 'https://api.themoviedb.org/3'
  path = '/movie/popular'
  params = {
  'api_key' : '54a9fff1e7fa56a1b0a2cc7c70c99ac4', 
  'language' : 'ko-KR'
  }
  response = requests.get(base_url+path, params=params).json()
  info = response.get('results') #리스트

  list1 = sorted(info, key = lambda movie : movie['vote_average'], reverse=True) #reverse=true 내림차순
  #유명한 영화 중 키를 람다함수 사용(k는 파라미터) 를 평점 높은 순으로 정렬
  #sort: 원본을 변형시켜 정렬
  #sorted: 원본 변형시키지 않고 괄호 안에 반복 가능한 자료형 입력
  #둘 다 key, reverse를 매개변수로 가질 수 있고 key값으로 정렬되며 lamda를 가질 수 있음
  #lamda는 특정 기준을 잡아줌

  list2 = [] 
  for i in range(5): #5개 추출
    #list1이 리스트이기 때문
    list2.append(list1[i]) #리스트1에서 추출한 i를 list2에 넣어둠
  return list2

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
