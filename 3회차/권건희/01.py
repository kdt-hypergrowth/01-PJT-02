import requests


def popular_count():
    url='https://api.themoviedb.org/3/movie/popular?api_key=136cf5bd6cbdc37e9588f804c3966f77'
    response=requests.get(url).json()
    a=response["results"]
    b=len(a)
    return b
    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
