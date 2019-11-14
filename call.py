import requests_async as requests
import asyncio
import time
  
# api-endpoint 
URL_reg = 'http://127.0.0.1:3500/api/v1/book'
URL_list = 'http://127.0.0.1:3500/api/v1/booklist'

async def register_book(name, ISBN):
    PARAMS = {'name':name, 'ISBN': ISBN}
    print('Starting request')
    r = await requests.post(url = URL_reg, params = PARAMS)
    await asyncio.sleep(5)
    print('Done')
    data = r.json() 
    return data

def get_books():
    r = requests.get(url = URL_list)
    data = r.json()
    print(data)

def process_future(future):
    print(future.result())


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    tasks = []
    me = []
    for i in range(5):
        tasks.append(loop.create_task(register_book('a', f'123{i}')))
    loop.run_until_complete(asyncio.gather(*tasks))
    print(tasks)
    print(tasks[0].result())