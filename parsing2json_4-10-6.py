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

pagen = get_pagen(url, shema)

card_links = []
for page in pagen:
  soup = get_soup(page)

  cards = soup.find_all('div', class_='item')
  for card in cards:
    card_link = shema + card.find('a', class_='name_item')['href']
    card_links.append(card_link)

data_json = []
for card_link in card_links:
  description_json = []

  item = get_soup(card_link)

  name = item.find('p', id='p_header').text
  article = item.find('p', class_='article').text.split(': ')[1]

  description = item.find('ul', id='description').find_all('li')
  
  for li in description:
    spec_name = li.text.split(':')[0].strip()
    spec = li.text.split(':')[-1].strip()
    description_json.append(
        {spec_name: spec}
    )
  
  in_stock = item.find('span', id='in_stock').text.split(': ')[1]
  price = item.find('span', id='price').text
  old_price = item.find('span', id='old_price').text
  link = card_link

  result_json = {
      'name': name,
      'article': article,
      'description': description_json,
      'in_stock': in_stock,
      'price': price,
      'old_price': old_price,
      'link': link
  }

  data_json.append(result_json) 

# сохраняем данные в json-файл
with open('res.json', 'w', encoding='utf-8') as file:
    json.dump(data_json, file, indent=4, ensure_ascii=False)