import requests


def popular_count():
    pass 
    # 여기에 코드를 작성합니다.  

BASE_URL = 'https://api.themoviedb.org/3/'
path = 'movie/popular'
params = {
        'api_key': 'a986250901395deffed1ae6e646ae735',
        'language': 'ko-KR'
}
response = requests.get(BASE_URL+path, params=params).json() # response에 api사이트에서 영화 popular api를 json형식으로 가져옴
response2 = response.get('results')         # response2에 딕셔너리들중 result만 가져옴

result = 0

for i in response2:
    result += 1
print(result)

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
