import requests

Base_URL = 'https://api.themoviedb.org/3'
path = '/movie/popular'
params ={
    'api_key': '652241f716c0f8b8f5006465a644f600',
    'language': 'en-en'
}
# popular는 TMDB에서 있는 영화 중 유명한 영화를 JSON 형태로 가지고 온 것
response = requests.get(Base_URL+path, params = params).json()

def popular_count():
    pass
    mov_list = []                           # list를 만들어준다
    results = response.get('results')       # 1. Page와 Results라는 key 2개가 먼저 있는데, Results를 꺼내온다
    for r in results:                       # 2. results는 리스트이라서, 딕셔너리로 타입 변환을 해준다
        movies = r.get('original_title')    # 3. 딕셔너리에 있는 key들 중 'original_title'을 가지고 온다
        mov_list.append(movies)             # 4. 영화 제목들을 만들어 놓은 리스트에 넣어 둔다
    return len(mov_list)                    # 5. 리스트의 길이를 구하고, 그것이 유명한 영화 개수이다


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
print(popular_count())
# 20
