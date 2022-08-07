import requests


def popular_count():
    Base_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key' : '036cba43a53da3f3d64b768b2cc83862',
        'language' : 'ko-KR'
    }
    # respnse의 dict_keys(['page', 'results', 'total_pages', 'total_results'])
    # 그중 영화정보가 담겨있는 results키의 value는 리스트라서
    # len으로 갯수를 받아온다.
    # print(len(response.get('results')))
    response = requests.get(Base_URL + path, params=params).json()
    return len(response.get('results'))
    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
