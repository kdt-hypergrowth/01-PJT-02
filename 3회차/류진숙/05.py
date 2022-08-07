import requests
from pprint import pprint


def credits(title):
    pass 
    # 여기에 코드를 작성합니다.  

    # 영화 제목 검색, 해당 영화 출연진, 스태프 중 연출진으로 구성된 목록 추출
    # 출연진 중 cast_id 값이 10 미만인 출연진만 추출 
    # 연출진은 department - directing인 데이터만 추출
    # 딕셔너리에 추출된 값을 리스트로 출력
    
    url = 'https://api.themoviedb.org/3'
    PATH = '/search/movie'
    movie_info = {
    'api_key' : '',
    'language' : 'ko-KR',
    'query' : title
    }

    response = requests.get(url+PATH, params=movie_info).json().get('results')

    if response:
        movie_id = response[0]['id']
        url_1 = 'https://api.themoviedb.org/3'
        PATH_1 = f'/movie/{movie_id}/credits'
        movie_info_= {
        'api_key' : 'bd811fbe5b564377261911e60b32d7ec',
        'language' : 'ko-KR',
        }

        response_1 = requests.get(url_1+PATH_1, params=movie_info_).json()

        
        final_cast_crew = {'cast' : [], 'crew' : []}
        for cast in response_1['cast']:
            if cast['cast_id'] < 10:
                final_cast_crew['cast'].append(cast['name'])
        for crew in response_1['crew']:
            if crew['department'] == 'Directing':
                final_cast_crew['crew'].append(crew['name'])
        
        return final_cast_crew
    
    else:
        None
     

                

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
