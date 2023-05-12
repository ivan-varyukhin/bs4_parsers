from bs4 import BeautifulSoup
import requests
import lxml
import csv


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

shema = 'http://parsinger.ru/html/'

urls = ['http://parsinger.ru/html/index1_page_1.html',
       'http://parsinger.ru/html/index2_page_1.html',
       'http://parsinger.ru/html/index3_page_1.html',
       'http://parsinger.ru/html/index4_page_1.html',
       'http://parsinger.ru/html/index5_page_1.html']

pagen = []

for url in urls:
  pagen.append(get_pagen(url, shema))

pagen = sum(pagen, []) #преобразуем список списков в простой список

data = []
for page in pagen:

  soup = get_soup(page)

  cards = soup.find_all('div', class_='item')
  for card in cards:
    try:
      name = card.find('a', class_='name_item').text.lstrip()
      description = card.find('div', class_='description').text.split('\n')
      brand = description[1].split(': ')[1].strip()
      spec_1 = description[2].split(': ')[1].strip()
      spec_2 = description[3].split(': ')[1].strip()
      spec_3 = description[4].split(': ')[1].strip()
      price = card.find('p', class_='price').text.replace(' руб', '').strip()
    except:
      pass

    data.append((name, brand, spec_1, spec_2, spec_3, price))
    
# сохраняем данные в csv-файл
with open('data.csv', 'w', encoding='utf-8-sig', newline='') as file:
  writer = csv.writer(file, delimiter=',')
  writer.writerows(data)