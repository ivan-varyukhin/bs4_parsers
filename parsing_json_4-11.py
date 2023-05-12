import requests


url = 'http://parsinger.ru/downloads/get_json/res.json'

response = requests.get(url=url).json()

categories = []

for item in response:
    categories.append(item["categories"])

categories = list(set(categories))

# categories = ['watch', 'mobile', 'mouse', 'hdd', 'headphones'] 
# к сожалению в задаче требуетс¤ определенный пор¤док

res1 = dict.fromkeys(categories, 0)
res2= dict.fromkeys(categories, 0)

for item in response:
  res1[item["categories"]] += int(item["count"])
  res2[item["categories"]] += int(item["count"])*int(item["price"].replace(' руб', ''))

print(' ол-во товаров: ', res1)
print('—тоимость товаров: ', res2)