import requests
#8854669b886a6c07c12ea947bcc2311d
URL='https://api.themoviedb.org/3'
path='/movie/popular'
params = {
    'api_key':'8854669b886a6c07c12ea947bcc2311d',
    'language' : 'KO-KR'
}
response=requests.get(URL+path, params=params).json()
print(response)
'''
def popular_count():
    pass 
    for

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
'''
