import requests
from pprint import pprint


def recommendation(title):
    # 검색할 수 없는 영화로 인해 오류가 발생하기에 트라이 익셉션 사용
    try:
        Base_URL = 'https://api.themoviedb.org/3'
        path = '/search/movie'
        params = {
            'api_key' : '036cba43a53da3f3d64b768b2cc83862',
            'language' : 'ko-KR',
            'query' : title
        }
        response = requests.get(Base_URL + path, params=params).json()
        m_id = response.get('results')[0].get('id')
        
        path2 = f'/movie/{m_id}/recommendations'
        params_2 = {
            'api_key' : '036cba43a53da3f3d64b768b2cc83862',
            'language' : 'ko-KR'
        }
        response2 = requests.get(Base_URL + path2, params=params_2).json()
        recommend = []
        for idx in response2.get('results'):
            recommend.append(idx.get('title'))
        return recommend
    # 검색결과 일치하는 영화가 없을때 IndexError: list index out of range 에러 발생
    # IndexError에러를 예외처리 
    except IndexError:
        return None
    

    # 여기에 코드를 작성합니다.  


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
    # # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
