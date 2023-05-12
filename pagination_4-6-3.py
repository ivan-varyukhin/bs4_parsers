# 4.6.3

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


url = 'http://parsinger.ru/html/index3_page_1.html'
shema = 'http://parsinger.ru/html/'

pagen = get_pagen(url, shema)

result = []

for i in range(len(pagen)):
  soup = get_soup(pagen[i])

  res = soup.find_all('a', class_='name_item')

  names = []

  for j in range(len(res)):
    names.append(res[j].text)
  result.append(names)

print(result)