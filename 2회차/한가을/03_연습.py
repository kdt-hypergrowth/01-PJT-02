# 특정 조건에 맞는 인기 영화 조회
# 인기 영화 목록을 평점이 높은 순으로 5개 정렬하여 영화 데이터 목록 출력
# 응답 받은 데이터 중 평점이 높은 영화 5개의 정보를 리스트로 반환하는 함수 작성

# 그러면 일단 정렬을 해서 평점이 높은 순으로 5개를 받아오자

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


def ranking():
    # 평점이 높은 순으로 영화 정보를 담을 리스트 초기화
    vote_average_top5 = []
    
    # 데이터를 딕셔너리로 형 변환
    movie_dict = response

    # 영화 데이터를 담고 있는 result를 리스트로 받아옴
    movie_details = movie_dict.get('results', None)
    
    # 람다 표현식을 화용해 movie_details의
    # 평점순으로 정렬된 딕셔너리를 리스트에 할당
    vote_avg = sorted(movie_details, key = lambda x : x['vote_average'], reverse = True)

    # 정렬된 딕셔너리에서 앞에 5개 값만 가져오기
    vote_average_top5 = vote_avg[:5]
    
    # 높은 평점 영화 5개 순으로 출력
    return vote_average_top5

if __name__ == '__main__':
    # popular 영화 평점순 5개 출력
    pprint(ranking())