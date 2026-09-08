import re
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup

start_time = time.perf_counter()

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
tbody = soup.find('tbody').find_all('tr')

columns = [th.text.strip().replace('؟', '') for th in table]
rows = [row.text.strip().split() for row in tbody]

api_url = (
    'https://api.tgju.org/v1/market/indicator/summary-table-data/price_dollar_rl'
)
for page in range(2, 20):
  params = {
      'lang': 'fa',
      'order_dir': 'desc',
      'start': (page - 1) * 30,
      'length': 30,
      'convert_to_ad': 1,
  }
  response = session.get(api_url, params=params, timeout=10)
  page_data = response.json().get('data', [])

  for item in page_data:
    clean_row = [re.sub(r'<[^>]*>', '', str(cell)).strip() for cell in item]
    rows.append(clean_row)

session.close()

df = pd.DataFrame(rows, columns=columns)
df.to_csv('Tgju_dolar.csv', index=False, encoding='utf-8-sig')

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f'Time for Run : {elapsed_time:.2f} s')