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


url = 'https://parsinger.ru/table/4/index.html'
shema = 'http://parsinger.ru/html/'

soup = get_soup(url)

cells = [float(x.text) for x in soup.find_all('td', class_='green')]

sum = 0

for cell in cells:
  sum += cell

print(round(sum, 3))