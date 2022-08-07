import requests
jeon="151"
url = f"https://api.themoviedb.org/3/movie/popular?api_key=<<api_key>>&language=en-US&page=1"
path='/get/movie/popular'
params={'api_key': '8854669b886a6c07c12ea947bcc2311d'
}
header0=f'Authorization: Bearer <<access_token>>'
response = requests.get(url,params=params)

print(response)


def popular_count():
    pass 
    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
