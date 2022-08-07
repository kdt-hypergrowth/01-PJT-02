# api : 0adf2f22b2273b1be4feadc7dc662e73
# https://api.themoviedb.org/3/movie/popular?api_key=<<api_key>>&language=en-US&page=1]


import requests

def popular_count():
    Base_url = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key':'0adf2f22b2273b1be4feadc7dc662e73',
        'language':'ko-KR'
    }
    response = requests.get(Base_url+path, params=params).json().get('results')
    return len(response)  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
