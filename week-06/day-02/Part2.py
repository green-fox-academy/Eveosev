import requests
from bs4 import BeautifulSoup
import collections as col

#Pbtech website
page = requests.get("https://www.pbtech.com/category/computers/laptops/shop-all?o=popularity")

page.content
soup = BeautifulSoup(page.content)
print(soup.prettify())
items = soup.find_all('div', attrs = {'class': 'products_list_wrapper expanded_list'})[0]

def clean_string(string):
    if '\n' in string:
        temp1 = string.replace('\n', '')
    temp2 = temp1.lstrip(' ')
    temp2 = temp2.rstrip(' ')
    return temp2

#extract the top three popular labtops
name_tree = items.find_all('div', attrs = {'class': 'item_content'})[0:3]
name_text = tuple(map(lambda x: x.find_all('a', attrs = {'class': 'item_line_name'})[0].get_text(), name_tree))
name = tuple(map(clean_string, name_text))
name

price_tree = items.find_all('span', attrs = {'class': 'price_full'})[0:6]
price = tuple(set(map(lambda x: x.get_text(), price_tree)))

laptop = col.namedtuple('laptop', ['name', 'previous_price', 'current_price'])

laptops = []
for i in range(len(name)):
    temp = tuple(laptop(name = name[i],
        current_price = price[i],
        previous_price = price[i]))
    laptops.append(temp)
laptops
