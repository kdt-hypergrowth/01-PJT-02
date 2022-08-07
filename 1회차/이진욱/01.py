from dotenv import load_dotenv
import os
import requests



def popular_count():
    URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular?'
    load_dotenv()
    pri_api_key = os.getenv('api_key')
    params = {
        'api_key' : pri_api_key
    } 
    
    response = requests.get(URL + path, params = params).json()
    ans = response.get('results')

    return len(ans)



if __name__ == '__main__':
    print(popular_count())
    # 20


#api 61c085220823244329dc47aa78df6c1c
# https://api.themoviedb.org/3/movie/550?api_key=61c085220823244329dc47aa78df6c1c