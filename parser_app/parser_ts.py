import requests
from bs4 import BeautifulSoup

URL = 'https://www.ts.kg/'

HEADERS = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
}

# 1 make request

def get_html(url, params=''):
    request = requests.get(url, headers=HEADERS, params=params)
    return request


# 2 get data
def get_data(html):
    bs = BeautifulSoup(html, features='html.parser')
    items = bs.find_all('div', class_='app-shows-item-full')
    ts_list = []
    for item in items:
        title = item.find('span', class_='app-shows-card-title').get_text(strip=True)
        info = item.find('span', class_='app-shows-card-tooltip').get_text(strip=True)
        ts_list.append({
            'title': title,
            'info': info,
        })
    return ts_list

# func parser
def parsing_ts():
    response = get_html(URL)
    if response.status_code == 200:
        ts_list2 = []
        for page in range(1, 2):
            response = get_html('https://www.ts.kg/category/films', params={'page': page})
            ts_list2.extend(get_data(response.text))
        return ts_list2
    else:
        raise Exception('Error in parsing ts')

# print(parsing_ts())