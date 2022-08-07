import requests


# API 키 값 = api_key=9c84ae21c51581335eb9aca74793ddb9
# TMDB 주소  https://api.themoviedb.org/3 
def popular_count():
    pass 
    from pprint import pprint
    base_url = 'https://api.themoviedb.org/3'  # During handling of the above exception, another exception occurred: url틀렸을때 
    path = '/movie/popular'                    # 인기있는 영화 목록

    params = { 
                'api_key' : '9c84ae21c51581335eb9aca74793ddb9',
                'language': 'ko-KR' #데이터 str을  한국어로 변경 
                } # 'Invalid API key: You must be granted a valid key.' 키없으면 키필요해 


    response= requests.get(base_url+path,params=params).json()# request.get (가져올 주소 + api 키를 딕셔너리로 넣어서 인증) .json의 형태로 가져온다


    pprint(len(response.get('results')))
    print (response)
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
