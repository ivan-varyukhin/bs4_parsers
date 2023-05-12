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


url = 'https://parsinger.ru/table/5/index.html'
shema = 'http://parsinger.ru/html/'

soup = get_soup(url)

# Получаем заголовки столбцов таблицы
headers = [header.text for header in soup.find_all('th')]

# Создаём пустой словарь для хранения сумм столбцов
result_dict = {header: 0.0 for header in headers}

# Получаем все строки таблицы
rows = soup.find_all('tr')

# Проходим по каждому столбцу
for col in range(len(headers)):
    # Проходим по каждой строке и добавляем значение в сумму для данного столбца
    for row in range(1, len(rows)):
        cell = rows[row].find_all('td')[col].text
        result_dict[headers[col]] += float(cell)

# Округляем значения до 3х символов после запятой
result_dict = {key: round(val, 3) for key, val in result_dict.items()}

print(result_dict)