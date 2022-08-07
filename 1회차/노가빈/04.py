import requests
from pprint import pprint


def recommendation(title):
    base_url = 'https://api.themoviedb.org/3/'
    path = f'search/movie?query={title}'
    params = {
        'api_key' : '09d0041de8747ddc735a2981381ae949',
        'language' : 'ko',
    }
    res = requests.get(base_url+path, params=params)
    data = res.json()

    #새 id를 가지고 data를 다시 가져오기 시작
    try:
        idResult = data['results'][0]['id']
        path = f'movie/{idResult}/recommendations'
        res = requests.get(base_url+path, params=params)
        data = res.json()
        dataList = []
        for i in data['results']:
            dataList.append(i['title'])
        return dataList
    except IndexError:
        return None


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
