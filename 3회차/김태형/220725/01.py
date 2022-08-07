import requests

api_key = "17d99d001f6c99dd0c99035720f60646"
url = f"https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=ko-KR&page=1"

def popular_count():
    pass 
    # 여기에 코드를 작성합니다.  
    res = (requests.get(url)).json()
    resResult = res['results']
    return len(resResult)
    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
