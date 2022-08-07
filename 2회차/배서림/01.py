# 01. 인기 영화 조회

# 인기 영화 목록의 개수를 출력합니다.
# requests 라이브러리를 활용하여 TMDB에서 현재 인기 있는 영화 목록(Get Populations) 데이터를 요청합니다.
# 응답 받은 데이터 영화 개수를 반환하는 함수를 작성합니다.


import requests

def popular_count():
    URL = 'https://api.themoviedb.org/3/movie/popular'
    params = {
        'api_key': '64960f74c1f585f363c60f7fa0745d1f',
    }

    response = requests.get(URL, params=params).json() # response 내의 object는 page, results, total_results, total_pages
    lst = response.get('results') # 원하는 값은 results 안에 있으므로 result 내의 것을 뽑아
    result = len(lst) # 값을 구함
    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
