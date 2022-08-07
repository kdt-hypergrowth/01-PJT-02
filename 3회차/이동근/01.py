from dotenv import load_dotenv
import os
import requests


def popular_count():
    # 여기에 코드를 작성합니다. 
    load_dotenv()
    
    key = os.getenv("KEY")

    params = {
        "api_key": key
    }

    baseURL = "https://api.themoviedb.org/3"
    specificURL = "/movie/popular"
    response = requests.get(baseURL + specificURL, params=params).json()

    return len(response["results"])


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
