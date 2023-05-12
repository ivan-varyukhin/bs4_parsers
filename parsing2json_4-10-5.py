from bs4 import BeautifulSoup
import requests
import lxml
import json

# получим суп
def get_soup(url):
  response = requests.get(url=url)
  response.encoding = 'utf-8'

  soup = BeautifulSoup(response.text, 'lxml')

  return soup

# получим пагинацию
def get_pagen(url, shema):

  soup = get_soup(url)
  
  pagen = soup.find('div', class_='pagen').find_all('a')
  pagen = [f"{shema}{link['href']}" for link in soup.find('div', class_='pagen').find_all('a')]

  return pagen

url = 'http://parsinger.ru/html/index1_page_1.html'
shema = 'http://parsinger.ru/html/'

soup = get_soup(url)
categories = [shema + category['href'] for category in
              soup.find('div', class_="nav_menu").find_all('a')]

pages = []
for category in categories:
  pagen = get_pagen(category, shema)
  pages.append(pagen)

pages = sum(pages, []) # конвертируем список списков в простой список

data_json = []

from tqdm.notebook import tqdm

for page in tqdm(pages, desc='Collecting data'):

  soup = get_soup(page)

  cards = soup.find_all('div', class_='item')
  for card in cards:
    try:
      name = card.find('a', class_='name_item').text.lstrip()
      description = card.find('div', class_='description').text.split('\n')
      spec_1 = description[1].split(': ')[1].strip()
      spec_1_name = description[1].split(': ')[0].strip()
      spec_2 = description[2].split(': ')[1].strip()
      spec_2_name = description[2].split(': ')[0].strip()
      spec_3 = description[3].split(': ')[1].strip()
      spec_3_name = description[3].split(': ')[0].strip()
      spec_4 = description[4].split(': ')[1].strip()
      spec_4_name = description[4].split(': ')[0].strip()
      price = card.find('p', class_='price').text.replace(' руб', '').strip()
    except:
      pass

    result_json = {
           'name': name,
           spec_1_name: spec_1,
           spec_2_name: spec_2,
           spec_3_name: spec_3,
           spec_4_name: spec_4,
           'price': price
        }

    data_json.append(result_json)

# сохраняем данные в JSON-файл
with open('res.json', 'w', encoding='utf-8') as file:
    json.dump(data_json, file, indent=4, ensure_ascii=False)