import requests
from bs4 import BeautifulSoup
from pandas.io.json import json_normalize
import json


def get_page_number():
    url= "http://api.zoopla.co.uk/api/v1/property_listings.json?county=Somerset&listing_status=sale&page_size=5&page_number=1&include_sold=1&api_key=mmfx23k4ka7v72xtwbztruu8"
    page =requests.get(url)
    df = json.loads(page.text)
    num = df['result_count']
    pages = int(round(num / 100, 0))
    return pages

def get_all_data(pages):
    df = []
    for i in range(1, pages + 1):
        url = "http://api.zoopla.co.uk/api/v1/property_listings.json?county=Somerset&listing_status=sale&page_size=100&page_number=" + str(i) + "&api_key=mmfx23k4ka7v72xtwbztruu8"
        page =requests.get(url)
        temp = json.loads(page.text)
        df.extend(temp['listing'])
    return df

