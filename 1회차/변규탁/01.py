import requests

# 26eaac93f79c23ac640e6c7c91fb93af
url = 'https://api.themoviedb.org/3'
path = '/movie/popular'
params = {
    'api_key': '26eaac93f79c23ac640e6c7c91fb93af',
    'language': 'ko-KR'
}

def popular_count():
    title_list = []
    response = requests.get(url+path, params=params).json()
    for data in response.get('results'):
        title_list.append(data.get('title'))
    return len(title_list)


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
