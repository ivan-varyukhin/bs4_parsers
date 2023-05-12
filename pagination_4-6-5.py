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


summa = 0

index_labels = {1: "watch", 2: "mobile", 3: "mouse", 4: "hdd", 5: "headphones"}
for i in range(5):
    for j in range(32):
        url = f"https://parsinger.ru/html/{index_labels[i+1]}/{i+1}/{i+1}_{j+1}.html"

        response = requests.get(url=url)
        response.encoding = 'utf-8'

        soup = BeautifulSoup(response.text, 'lxml')

        price = soup.find('span', id='price').text
        price = price.replace(" руб","")

        amount = soup.find('span', id='in_stock').text
        amount = amount.replace("В наличии: ","")

        sum = float(price) * int(amount)

        print('Анализирую страницу:', url, '...')
        print('Цена: ', price, ' | ', 'Количество: ', amount, ' | ', 'Итого: ', sum)
        print('***')

        summa += sum

print('Общая стоимость всех товаров: ', summa)