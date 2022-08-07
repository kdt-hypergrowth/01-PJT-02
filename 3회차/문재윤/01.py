import requests


def popular_count():
    
    # 여기에 코드를 작성합니다.  
 params = {'api_key' : '6536d1c9342b7cc9209b1ef937331746',
    'language' : 'ko',
    'page' : '1',
    'region' : 'KR'}

 url = 'https://api.themoviedb.org/3/movie/popular'
 response = requests.get(url, params= params)
 data = response.json()['results']

#  print(type(data))
#  t = len(data)
 return(len(data))
 

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
