# 인기 영화 목록 중 평점이 8점 이상인 영화 목록 출력
# 평점 : vote_average

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

#pprint(data)

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

if __name__ == '__main__':
    pprint(vote_average_movies())