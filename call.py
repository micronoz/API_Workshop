import requests
import time

# api-endpoint
URL_reg = 'http://127.0.0.1:3500/api/v1/book'
URL_list = 'http://127.0.0.1:3500/api/v1/booklist'

async def register_book(name, ISBN):
    PARAMS = {'name':name, 'ISBN': ISBN}
    r = requests.post(url = URL_reg, params = PARAMS)
    data = r.json()
    return data

def get_books():
    r = requests.get(url = URL_list)
    data = r.json()
    print(data)
