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

category_urls = [shema + category['href'] for category in soup.find('div', class_="nav_menu").find_all('a')]
category_names = [category['id'] for category in soup.find('div', class_="nav_menu").find_all('div')]

categories = dict(zip(category_names, category_urls))

category_pages = {}

for category_name in category_names:
    category_url = categories[category_name]
    pagen = get_pagen(category_url, shema)
    card_links = []
    for page in pagen:
      soup = get_soup(page)
      cards = soup.find_all('div', class_='item')

      for card in cards:
        card_link = shema + card.find('a', class_='name_item')['href']
        card_links.append(card_link)
    category_pages[category_name] = card_links

data_json = []

for category_name in category_pages:
  for card_link in category_pages[category_name]:
      description_json = []

      item = get_soup(card_link)

      name = item.find('p', id='p_header').text
      article = item.find('p', class_='article').text.split(': ')[1]

      description = item.find('ul', id='description').find_all('li')
  
      for li in description:
        spec_name = li['id']
        spec = li.text.split(':')[-1].strip()
        description_json.append(
            {spec_name: spec}
        )
  
      in_stock = item.find('span', id='in_stock').text.split(': ')[1]
      price = item.find('span', id='price').text
      old_price = item.find('span', id='old_price').text
      link = card_link

      descr = {k:v for element in description_json for k,v in element.items()}

      result_json = {
          'categories': category_name,
          'name': name,
          'article': article,
          'description': descr,
          'in_stock': in_stock,
          'price': price,
          'old_price': old_price,
          'link': link
      }

      data_json.append(result_json)  

# сохраняем данные в json-файл
with open('res.json', 'w', encoding='utf-8') as file:
    json.dump(data_json, file, indent=4, ensure_ascii=False)