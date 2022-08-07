import requests


def popular_count():
    pass 
    # 여기에 코드를 작성합니다.  
Base_URL = 'https://api.themoviedb.org/3'
path = '/movie/popular'
params = {
    'api_key': '223131069bc4ff601e73529b7eb1b275',
}
response = requests.get(Base_URL+path, params = params).json()
print(len(response['results']))

# 밑에 수정하지 말아야 하는 코드에 있는 if 로 시작되는 method를 이해하지 못했다.
# count method를 이용해서 영화를 새려고 하는 것 같은데 아직은 잘 모르겠다.
# if, while 공부 후 다시 확인

# # 아래의 코드는 수정하지 않습니다.
# if __name__ == '__main__':
#     """
#     popular 영화목록의 개수 반환
#     """
#     print(popular_count())
#     # 20

# Alt 1
# import requests

# def popular_count():
#     pass 
#     # 여기에 코드를 작성합니다.  
#     Base_URL = 'https://api.themoviedb.org/3'                                   # I forgot to use `tab`` since it was `def` section.
#     path = '/movie/popular'                                                     # If I define my code with `return` function,
#     params = {                                                                  # I can print out the value that I was looking for
#     'api_key': '223131069bc4ff601e73529b7eb1b275',
#     }
#     response = requests.get(Base_URL+path, params = params).json()
#     return (len(response['results']))

# if __name__ == '__main__':
#     """
#     popular 영화목록의 개수 반환
#     """
#     print(popular_count())