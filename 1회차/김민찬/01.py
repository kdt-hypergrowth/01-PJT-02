import requests

def popular_count():
    # 여기에 코드를 작성합니다. 
    
    params = {
        "api_key": '8854669b886a6c07c12ea947bcc2311d',
        'language': 'ko-KR'
    }

    BaseURL = "https://api.themoviedb.org/3"
    path = "/movie/popular"
    response = requests.get(BaseURL + path, params = params).json()

    return len(response['results'])


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20