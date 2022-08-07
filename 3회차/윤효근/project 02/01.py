import requests
from pprint import pprint
url = "https://api.themoviedb.org/3/movie/popular?api_key=484061e3049ebd762e6e4c9830eacfe4&language=ko-KR&page=1"
headers = {"Accept": "application/json"}

def popular_count():
    pass
    response = requests.get(url, headers=headers)
    m_list = response.json()
    movies=m_list['results']

    return len(movies)
    # 여기에 코드를 작성합니다.


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20