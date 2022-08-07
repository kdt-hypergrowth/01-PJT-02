import requests

# 인기 영화 목록의 개수를 출력합니다.
# requests 라이브러리를 활용하여 TMDB에서 현재 인기 있는 영화 목록(Get Populations) 데이터를 요청합니다.
# 응답 받은 데이터 영화 개수를 반환하는 함수를 작성합니다.

def popular_count():
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key' : '94ceed584568fa7a9113545f2e4291f5',
        'language' : 'ko-KR'
    }

    # 해당 BASE_URL에서 API request
    response = requests.get(BASE_URL+path, params=params)
    # 요청한 데이터들 json 형태로 저장
    movies = response.json()

    # {'page': 1, 'results': [{'adult': False, 'backdrop_path': '/393mh1AJ0GYWVD7Hsq5KkFaTAoT.jpg', 
    # 'genre_ids': [12, 28, 878], 'id': 507086, 'original_language': 'en', 'original_title': 'Jurassic World Dominion', 
    # 'overview': '어쩌구 저쩌구~', 'popularity': 11579.18, 'poster_path': '/odxdUZWZ7fBfy3ZRj063wuJnZvo.jpg', 'release_date': '2022-06-01', 
    # 'title': '쥬라기 월드: 도미니언', 'video': False, 'vote_average': 7, 'vote_count': 1794}, ...(생략)],
    # 'total_pages': 34407, 'total_results': 688125}

    # movies의 'results' 리스트에 접근한 후 그 리스트의 길이 출력
    return len(movies['results'])


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
