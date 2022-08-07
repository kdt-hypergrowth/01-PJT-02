
import requests
# https://api.themoviedb.org/3/movie/76341?api_key=<<api_key>>
# 7f4bcebe925d6be694eced873e49d10e
# https://api.themoviedb.org/3/movie/popular?api_key=<<api_key>>&language=en-US&page=1
BASE_URL = 'https://api.themoviedb.org/3/'
path = 'movie/popular'
params = {
    'api_key': '7f4bcebe925d6be694eced873e49d10e',
    'language': 'ko-KR'
}

# response = requests.get(BASE_URL+path, params=params)
# data = response.json()


# cnt = (data.get('results'))
# # print(list(data.get('results'))[0])

# s = []
# for i in range(20):
#     s.append(list(data.get('results'))[i]['title'])

# print(len(s))


def popular_count():
    pass
    # 여기에 코드를 작성합니다.
    response = requests.get(BASE_URL+path, params=params)
    data = response.json()

    # print(list(data.get('results'))[0])
    s = []
    for i in range(20):
        s.append(list(data.get('results'))[i]['title'])
    return len(s)


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
