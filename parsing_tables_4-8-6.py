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

orange_cells = [float(x.text) for x in soup.find_all('td', class_='orange')]
blue_cells = [float(x.text) for x in soup.select('td:last-child')]

sum = 0

for i in range(0, len(blue_cells)):
  mul = orange_cells[i]*blue_cells[i]
  sum += mul

print(round(sum, 3))