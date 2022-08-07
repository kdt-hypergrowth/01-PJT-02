import requests


def popular_count():

    # 여기에 코드를 작성합니다.  
    base_url = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key' : 'fea85eb7c3131ce04c5cfc321e34f64c',
        'language' : 'ko-KR',
    } 

    response = requests.get(base_url+path, params = params).json()

    cnt = 0

    for i in response.get('results'):
        cnt += 1
    
    return cnt
    # print(cnt)

    # print (response)
    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
