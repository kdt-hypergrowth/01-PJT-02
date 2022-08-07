import requests
from pprint import pprint


def recommendation(title):
    try:
        URL = 'https://api.themoviedb.org/3'
        path = '/search/movie'
        params = {
            'api_key': '344b9a7b0867ea18b1b9d6356fb7a1f0',
            'language': 'ko-KR',
            'query': title
        }
        response = requests.get(URL+path, params = params).json()      
        movie_id = response.get('results')[0].get('id')
        
        main_URL = 'https://api.themoviedb.org/3'
        main_path = f'/movie/{movie_id}/recommendations'
        params = {
            'api_key': '344b9a7b0867ea18b1b9d6356fb7a1f0',
            'language': 'ko-KR',
        }
        main_response = requests.get(main_URL+main_path, params = params).json()
        name_list = []
        for a in main_response.get('results'):
            name_list.append(a.get('title'))
        return name_list
    except: 
        return 'None'

if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    print(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    print(recommendation('그래비티'))
    # []
    print(recommendation('검색할 수 없는 영화'))
    # None
