import requests
from bs4 import BeautifulSoup

URLS = ['https://www.epravda.com.ua/rus/news/2022/10/31/693273/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374322/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374321/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374320/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374318/',
        'https://www.eurointegration.com.ua/rus/news/2022/10/31/7149731/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374315/',
        'https://www.epravda.com.ua/rus/news/2022/10/31/693267/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374313/',
        'https://www.pravda.com.ua/rus/articles/2022/10/31/7374199/',
        'https://www.epravda.com.ua/rus/news/2022/10/31/693263/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374309/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374308/',
        'https://www.epravda.com.ua/rus/publications/2022/10/31/693211/',
        'https://life.pravda.com.ua/health/2022/10/31/251079/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374304/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374303/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374302/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374301/',
        'https://www.epravda.com.ua/rus/news/2022/10/31/693261/', 'https://tabloid.pravda.com.ua/focus/635fbe8ea5efe/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374297/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374296/',
        'https://life.pravda.com.ua/society/2022/10/31/251077/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374294/',
        'https://www.epravda.com.ua/rus/news/2022/10/31/693258/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374244/',
        'https://www.epravda.com.ua/rus/news/2022/10/31/693254/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374289/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374288/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374287/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374286/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374285/',
        'https://life.pravda.com.ua/society/2022/10/31/251076/',
        'https://www.epravda.com.ua/rus/news/2022/10/31/693253/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374282/',
        'https://www.eurointegration.com.ua/rus/news/2022/10/31/7149718/',
        'https://www.epravda.com.ua/rus/news/2022/10/31/693248/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374279/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374278/',
        'https://www.epravda.com.ua/rus/news/2022/10/31/693247/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374275/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374274/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374273/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374272/',
        'https://www.epravda.com.ua/rus/news/2022/10/31/693245/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374270/',
        'https://life.pravda.com.ua/society/2022/10/31/251075/',
        'https://www.epravda.com.ua/rus/news/2022/10/31/693244/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374267/',
        'https://www.epravda.com.ua/rus/news/2022/10/31/693242/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374265/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374264/',
        'https://www.eurointegration.com.ua/rus/news/2022/10/31/7149712/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374261/',
        'https://www.epravda.com.ua/rus/news/2022/10/31/693243/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374258/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374257/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374256/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374250/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374249/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374245/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374243/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374242/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374241/',
        'https://www.eurointegration.com.ua/rus/news/2022/10/31/7149699/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374239/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374238/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374236/',
        'https://life.pravda.com.ua/society/2022/10/31/251072/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374231/',
        'https://www.eurointegration.com.ua/rus/news/2022/10/31/7149698/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374228/',
        'https://www.eurointegration.com.ua/rus/news/2022/10/31/7149696/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374226/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374227/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374225/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374224/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374223/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374222/',
        'https://www.eurointegration.com.ua/rus/news/2022/10/31/7149695/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374220/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374219/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374218/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374217/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374216/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374215/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374190/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374214/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374213/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374212/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374211/',
        'https://www.pravda.com.ua/rus/news/2022/10/31/7374210/']


def get_links():
    all_links_article = []
    url = 'https://www.pravda.com.ua/rus/news/date_31102022/'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        articles = soup.find(name='div', class_='container_sub_news_list_wrapper').find_all('a')
    for a in articles:
        if 'https:' in a.get('href'):
            all_links_article.append(a.get('href'))
        else:
            all_links_article.append(f"https://www.pravda.com.ua{a.get('href')}")
    return all_links_article


def get_data() -> list[dict]:
    all_data = []
    for url in URLS:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            if 'epravda.com.ua' in url:
                title = soup.find(name='h1').text.replace("\r", "").replace("\n", "")
                views = soup.find(name='div', class_='content_column').find(name='div', class_='post__views').text
                date_time = soup.find(name='div', class_='post__time').text
                date = url.split('/')
                time_article = date_time.split(',')[2].split('-')[0].strip()
                created = int(date[-5]), int(date[-4]),  int(date[-3]),  int(time_article.split(':')[0]),  int(time_article.split(':')[1])
                all_data.append({'title': title, 'created': created, 'link_news': url, 'views': views.split(' ')[0]})
            elif 'www.pravda.com.ua' in url:
                title = soup.find(name='h1').text.replace("\r", "").replace("\n", "")
                views = soup.find(name='div', class_='post_views').text
                date_time = soup.find(name='div', class_='post_time').text
                date = url.split('/')
                time_article = date_time.split(',')[-1].strip()
                created =  int(date[-5]),  int(date[-4]),  int(date[-3]),  int(time_article.split(':')[0]),  int(time_article.split(':')[1])
                all_data.append({'title': title, 'created': created, 'link_news': url, 'views': views.split(' ')[0]})
    return all_data


# if __name__ == '__main__':
#     # links = get_links()
#     # print(links)
# data_for_db = get_data()
