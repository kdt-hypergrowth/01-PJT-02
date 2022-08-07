from pprint import pprint
import requests

URL = 'https://api.themoviedb.org/3'
path = '/movie/popular'
params ={
    'api_key' : 'd84fbf5eb517d499e6c3ce37311d4394',
    'language' : 'ko-KR'
}

response = requests.get(URL + path, params = params).json()
data = response.get('results')


def vote_average_movies():
        # 평점 8 이상인 영화 목록을 담는 리스트 초기화
    vote_average_over_8 = []

    # 받아온 데이터를 딕셔너리로 형 변환
    movie_dict = response

    # movie_dict에서 영화 데이터를 담고 있는
    # result를 리스트로 받아옴
    movie_details = movie_dict.get('results', None)
    
    # movie_details 반복
    for movie_derail in movie_details:
        # 개별 영화들의 평점 확인
        vote_average = movie_derail.get('vote_average', None)
        # 8점 이상인 경우 vote_average_over_8에 해당 영화 정보를 담는다
        if vote_average >= 8:
            vote_average_over_8.append(movie_derail)
    # 평점 8 이상인 영화들의 목록을 담은 리스트를 반환
    return vote_average_over_8
    # 여기에 코드를 작성합니다.  


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
