import requests
from pprint import pprint


def recommendation(title):
    pass 
    # 여기에 코드를 작성합니다.  
    Base_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params={
        'api_key':'9e7ad8abf0f44312c8921229635fe29f',
        'language':'ko-KR',
        'query': title }
    response = requests.get(Base_URL+path, params=params).json().get('results')

    if not response: # response가 비어있으면 none 반환
        return None
    movie_id = response[0].get('id')
    path_1=f'/movie/{movie_id}/recommendations' # recommenadation을 위한 API GET에 해당하고 {}를 통해 바뀌는 값을 넣어준다.
    response1=requests.get(Base_URL + path_1, params=params).json().get('results')
    Titles=[]
    for i in response1:
        Titles.append(i.get('title'))
    if Titles ==[]:
        return []
    else:
        return Titles


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
