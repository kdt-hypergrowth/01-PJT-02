import requests
import os
from pprint import pprint
from dotenv import load_dotenv


def popular_count():
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={api_key}"
    response = requests.get(url).json() # 먼저 출력 후 json 구조 파악

    # pprint(response)

    pop_movies = response["results"] # 인기있는 영화들의 딕셔너리들로 이뤄진 리스트  
    num = len(pop_movies)
    
    return num

if __name__ == '__main__':
    load_dotenv()
    api_key = os.getenv('api_key')

    print(popular_count())
    # 20
