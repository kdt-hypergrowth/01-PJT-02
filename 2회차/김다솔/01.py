import requests


def popular_count():
    pass 
# 여기에 코드를 작성합니다.  
    base_url = 'https://api.themoviedb.org/3'
    path= '/movie/popular'
    params = {
        'api_key': 'ae586975d1f9e85b3c63bafccb20d3d0',
        'language' : 'ko-KR'
    }
    # result 키의 벨류 = 리스트 안에 영화딕셔너리
    response = requests.get(base_url+path, params = params).json() 
    value = response.get('results')
    return len(value)  # len() 리스트 요소의 개수
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
