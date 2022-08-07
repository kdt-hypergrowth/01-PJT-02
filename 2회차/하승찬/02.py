import requests
from pprint import pprint
# API 키 값 = api_key=9c84ae21c51581335eb9aca74793ddb9
# TMDB 주소  https://api.themoviedb.org/3

def vote_average_movies():
    pass 

base_ulr ='https://api.themoviedb.org/3'
path = '/movie/popular'   
params = {
  'api_key' : '9c84ae21c51581335eb9aca74793ddb9',
  'language' : 'ko-KR'
}

response = requests.get(base_ulr+path,params=params).json()

# 먼저 영화의 평점 vote averge를 가져와서 if문으로 비교후 8이 넘는다면 
#bote_movie로 옮긴다. 포문으로 영화의 갯수를 측정한 후
# for문으로 영화의 평점을 뽑은 뒤  
#각각의 영화를 평점의 value값을 if문으로 비교 비교 후 8점이 넘는 영화는
# 보관함으로 이동하자  
movies = (response.get('results')) # movies는 주소에서 가져온 영화들의 값들
bote_movie = []                    # bote_movie에 8점이 넘는 영화를 보관

for i in range(len(movies)):       #for문으로 영화의 갯수만큼 반복문을 돌림
  if movies[i].get('vote_average') >= 8:   #영화에 평점이 8이 넘는다면 bote_movie보관함에 더해준 후 마지막에 프린트 
    bote_movie.append(movies[i])
pprint(bote_movie)




# movies_vote

# print(movies,type(movies))


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
