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


# 4.6.4
url = 'http://parsinger.ru/html/index3_page_4.html'
shema = 'http://parsinger.ru/html/'

pagen = get_pagen(url, shema)

list_link = []

for i in range(len(pagen)):
  soup = get_soup(pagen[i])

  pages = soup.find_all('a', class_='name_item')

  for link in pages:
    list_link.append(f"{shema}{link['href']}")

summa = 0

for link in list_link:
  soup = get_soup(link)

  art = soup.find('p', class_='article').text
  art = art.replace("јртикул: ","")

  summa = summa + int(art)

print('—умма:', summa)