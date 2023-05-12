from bs4 import BeautifulSoup
import requests
import lxml
import csv, json


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


data = []
for page in pagen:
  soup = get_soup(page)

  cards = soup.find_all('div', class_='item')
  for card in cards:
    try:
      name = card.find('a', class_='name_item').text.lstrip()
      description = card.find('div', class_='description').text
      brand = description.split(': ')[1].split('\n')[0].strip()
      form_factor = description.split(': ')[2].split('\n')[0].strip()
      capacity = description.split(': ')[3].split('\n')[0].strip()
      buffer_size = description.split(': ')[4].split('\n')[0].strip()
      price = card.find('p', class_='price').text.replace(' руб', '').strip()
    except:
      pass

    data.append((name, brand, form_factor, capacity, buffer_size, price))

# сохраняем данные в csv-файл
with open('data.csv', 'w', encoding='utf-8-sig', newline='') as file:
  writer = csv.writer(file, delimiter=';')
  writer.writerow(('Наименование', 'Бренд', 'Форм-фактор', 'Ёмкость', 'Объём буф. памяти', 'Цена'))
  writer.writerows(data)