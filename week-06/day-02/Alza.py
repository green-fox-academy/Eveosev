import requests
from bs4 import BeautifulSoup
import collections as col

#Gaming
page = requests.get("https://www.alza.co.uk/gaming-laptops/18848814.htm")

page.content
soup = BeautifulSoup(page.content)
print(soup.prettify())

#extract the top three laptops
first_laptop = soup.find_all('div', attrs = {'class': 'box browsingitem centeredPrice canBuy inStockAvailability first firstRow'})
second_laptop = soup.find_all('div', attrs = {'class': 'box browsingitem centeredPrice canBuy inStockAvailability firstRow'})
third_laptop = soup.find_all('div', attrs = {'class': 'box browsingitem centeredPrice canBuy inStockAvailability last firstRow'})

top_three_laptops = [first_laptop, second_laptop, third_laptop]

laptop = col.namedtuple('laptop', ['name', 'previous_price', 'current_price'])

laptops = []
for i in top_three_laptops:
    temp = tuple(laptop(name = i[0].find_all('a', attrs = {'class': 'name browsinglink'})[0].get_text(),
        previous_price = i[0].find_all('span', attrs = {'class': 'np2'})[0].get_text(),
        current_price = i[0].find_all('span', attrs = {'class': 'c2'})[0].get_text()))
    laptops.append(temp)
laptops


#Home and office
page = requests.get("https://www.alza.co.uk/basic-home-and-office-laptops/18843464.htm")

page.content
soup = BeautifulSoup(page.content)
print(soup.prettify())

#extract the top three laptops
first_laptop = soup.find_all('div', attrs = {'class': 'box browsingitem centeredPrice canBuy inStockAvailability first firstRow'})
second_laptop = soup.find_all('div', attrs = {'class': 'box browsingitem centeredPrice canBuy inStockAvailability firstRow'})
third_laptop = soup.find_all('div', attrs = {'class': 'box browsingitem centeredPrice canBuy inStockAvailability last firstRow'})

top_three_laptops = [first_laptop, second_laptop, third_laptop]

laptop = col.namedtuple('laptop', ['name', 'previous_price', 'current_price'])

laptops = []
for i in top_three_laptops:
    temp = tuple(laptop(name = i[0].find_all('a', attrs = {'class': 'name browsinglink'})[0].get_text(),
        previous_price = i[0].find_all('span', attrs = {'class': 'np2'})[0].get_text(),
        current_price = i[0].find_all('span', attrs = {'class': 'c2'})[0].get_text()))
    laptops.append(temp)
laptops


#Home and office
page = requests.get("https://www.alza.co.uk/professional-laptops/18853299.htm")

page.content
soup = BeautifulSoup(page.content)
print(soup.prettify())

#extract the top three laptops
first_laptop = soup.find_all('div', attrs = {'class': 'box browsingitem centeredPrice canBuy inStockAvailability first firstRow'})
second_laptop = soup.find_all('div', attrs = {'class': 'box browsingitem centeredPrice canBuy inStockAvailability firstRow'})
third_laptop = soup.find_all('div', attrs = {'class': 'box browsingitem centeredPrice canBuy inStockAvailability last firstRow'})

top_three_laptops = [first_laptop, second_laptop, third_laptop]

laptop = col.namedtuple('laptop', ['name', 'previous_price', 'current_price'])

laptops = []
for i in top_three_laptops:
    temp = tuple(laptop(name = i[0].find_all('a', attrs = {'class': 'name browsinglink'})[0].get_text(),
        previous_price = i[0].find_all('span', attrs = {'class': 'np2'})[0].get_text(),
        current_price = i[0].find_all('span', attrs = {'class': 'c2'})[0].get_text()))
    laptops.append(temp)
laptops
