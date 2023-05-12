from bs4 import BeautifulSoup
import requests
import lxml

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
    #print(card_link)
    card_links.append(card_link)

data = []
for card_link in card_links:
  item = get_soup(card_link)

  name = item.find('p', id='p_header').text
  article = item.find('p', class_='article').text.split(': ')[1]

  brand = item.find('li', id='brand').text.split(': ')[1]
  model = item.find('li', id='model').text.split(': ')[1]
  type = item.find('li', id='type').text.split(': ')[1]
  display = item.find('li', id='display').text.split(': ')[1]
  material_frame = item.find('li', id='material_frame').text.split(': ')[1]
  material_bracer = item.find('li', id='material_bracer').text.split(': ')[1]
  size = item.find('li', id='size').text.split(': ')[1]
  site = item.find('li', id='site').text.split(': ')[1]

  in_stock = item.find('span', id='in_stock').text.split(': ')[1]
  price = item.find('span', id='price').text
  old_price = item.find('span', id='old_price').text
  link = card_link

  data.append((name, article, brand, model, type, display, material_frame, material_bracer, size, site, in_stock, price, old_price, link)) 

# сохраняем данные в csv-файл
headers = [
    'Наименование', 'Артикул', 'Бренд', 'Модель', 'Тип', 'Технология экрана', 
    'Материал корпуса', 'Материал браслета', 'Размер', 'Сайт производителя', 
    'Наличие', 'Цена', 'Старая цена',  'Ссылка на карточку с товаром'
    ]
with open('data.csv', 'w', encoding='utf-8-sig', newline='') as file:
  writer = csv.writer(file, delimiter=',')
  writer.writerow(headers)
  writer.writerows(data)