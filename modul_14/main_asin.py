import requests
import platform
from bs4 import BeautifulSoup
import time
import asyncio
import aiohttp
from fake_useragent import UserAgent
from memory_profiler import profile

start_time = time.time()
ua = UserAgent(browsers=['chrome', 'edge', 'internet explorer', 'firefox', 'safari', 'opera'])
headers = {'user-agent': ua.random}
print(headers)
url = 'https://quotes.toscrape.com'
store_ = []


async def collect_data():
    async  with aiohttp.ClientSession(headers=headers) as session:
        tasks = []
        for n_page in range(1, 11):
            task = asyncio.create_task(parse_date(session, n_page))
            tasks.append(task)
        await asyncio.gather(*tasks)
            # print(f'Page: {n_page}')
            # response = await requests.get(f"{url}/page/{n_page}/")
            # parse_date(response)

async def parse_date(session: aiohttp.ClientSession, page: int):
    url_ = f"{url}/page/{page}/"
    async with session.get(url=url_) as response:
        response_text = await response.text()
        soup = BeautifulSoup(response_text, 'lxml')
        quotes = soup.find_all('span', class_='text')
        authors = soup.find_all('small', class_='author')
        tags = soup.find_all('div', class_='tags')
        authors_href = soup.find_all('div', class_='quote')
        for i in range(0, len(quotes)):
            quote = quotes[i].text.replace("“", "").replace("”", "").replace("\r", "").replace("\n", "")
            author = authors[i].text
            list_tag = []
            tagsforquotes = tags[i].find_all('a', class_='tag')
            for tagforquote in tagsforquotes:
                list_tag.append(tagforquote.text)
            for a in authors_href[i].find_all('a'):
                if a.text == '(about)':
                    href = f"{url}{a['href']}"
            store_.append({"quote": quote,
                           "author": author,
                           "tag": list_tag,
                           "href": href})
        print(f'INFO page number {page}')

@profile
def main():
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(collect_data())
    # asyncio.get_running_loop().run_until_complete(collect_data())
    for el in store_:
        print(el)
    print(time.time() - start_time)


if __name__ == '__main__':
    main()

