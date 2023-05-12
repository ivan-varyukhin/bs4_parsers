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

url = 'https://parsinger.ru/html/index4_page_1.html'
shema = 'http://parsinger.ru/html/'

pagen = get_pagen(url, shema)

data_json = []
for page in pagen:
  soup = get_soup(page)

  cards = soup.find_all('div', class_='item')
  for card in cards:
    name = card.find('a', class_='name_item').text.lstrip()
    description = card.find('div', class_='description').text
    brand = description.split(': ')[1].split('\n')[0].strip()
    form_factor = description.split(': ')[2].split('\n')[0].strip()
    capacity = description.split(': ')[3].split('\n')[0].strip()
    price = card.find('p', class_='price').text.replace(' руб', '').strip()

    result_json = {
        'name': name,
        'brand': brand,
        'form_factor': form_factor,
        'capacity': capacity,
        'price': price

    }

    data_json.append(result_json)

# сохраняем данные в JSON-файл
with open('res.json', 'w', encoding='utf-8') as file:
    json.dump(data_json, file, indent=4, ensure_ascii=False)