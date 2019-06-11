# Bara a flight home: She lives in Bristol, UK and would like to go to Prague, CZ for Christmas this year. 
# She prefers to arrive to the city within 5 days prior to 24.12. 
# and save as much money as possible. No changes in flights, please.
import requests
import json
import pandas as pd
from pandas.io.json import json_normalize
from datetime import datetime

baseurl = 'https://api.skypicker.com/flights?flyFrom=BRS&to=PRG&dateFrom=18/12/2019&dateTo=23/12/2019&max_stopovers=0&partner=picky'
data = requests.get(baseurl)

df = json.loads(data.text)
flights_data = df['data']

price_list = list(map(lambda x: x['price'], flights_data))
min_price = min(price_list)
index = price_list.index(min_price)

#Cheapest flight
cheapest_flight = flights_data[index]

cheapest_flight['dTime'] = datetime.fromtimestamp(cheapest_flight['dTime']).strftime('%Y-%m-%d %H:%M:%S')
cheapest_flight['aTime'] = datetime.fromtimestamp(cheapest_flight['aTime']).strftime('%Y-%m-%d %H:%M:%S')

print(cheapest_flight)