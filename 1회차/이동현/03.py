import requests
from pprint import pprint


def ranking():
    pass 
    # 여기에 코드를 작성합니다.  

BASE_URL = 'https://api.themoviedb.org/3/'
path = 'movie/popular'
params = {
        'api_key': 'a986250901395deffed1ae6e646ae735',
        'language': 'ko-KR'
}
response = requests.get(BASE_URL+path, params=params).json() # response에 api사이트에서 영화 popular api를 json형식으로 가져옴
response2 = response.get('results')         # response2에 딕셔너리들중 result만 가져옴

result = []

for i in response2:                                # 평점을 모아서 순서대로 정렬
  result.append(i['vote_average'])
  result = sorted(result)       

new_result = []
for ii in range(1, 6):                              # 평점 상위 5개만 추려서 new_result 만듬
  new_result.append(result[len(result) - ii ])  

final_result = []
for iii in response2:                               # new_result에 있는 상위 평점 5개의 점수와 같은 영화를 검색
  if iii['vote_average'] in new_result:
    final_result.append(iii)
pprint(final_result) 


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
