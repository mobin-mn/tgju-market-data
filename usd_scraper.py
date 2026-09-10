import re
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup

session = requests.Session()

headers = {
    'User-Agent': (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,'
        ' like Gecko) Chrome/152.0.0.0 Safari/537.36'
    ),
    'Referer': 'https://www.tgju.org/',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
}

session.headers.update(headers)


url = 'https://www.tgju.org/profile/price_dollar_rl/history'
response = session.get(url, timeout=10)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('thead').find_all('th')
columns = [th.text.strip().replace('؟', '') for th in table]

api_url = 'https://api.tgju.org/v1/market/indicator/summary-table-data/price_dollar_rl'
target_date = input('Enter start date (YYYY/MM/DD, e.g. 1403/06/24): ').strip()
start_time = time.perf_counter()

rows = []
page = 1

while True:
    params = {
        'lang': 'fa',
        'order_dir': 'desc',
        'start': (page - 1) * 30,
        'length': 30,
        'from': target_date,
        'to': '',
        'convert_to_ad': 1,
    }

    response = session.get(api_url, params=params, timeout=10)
    page_data = response.json().get('data', [])

    if not page_data:
        break

    for item in page_data:
        clean_row = [re.sub(r'<[^>]*>', '', str(cell)).strip() for cell in item]
        rows.append(clean_row)

    page += 1

session.close()

df = pd.DataFrame(rows, columns=columns)
df.to_csv('Tgju_dolar.csv', index=False, encoding='utf-8-sig')

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f'Time for Run : {elapsed_time:.2f} s')