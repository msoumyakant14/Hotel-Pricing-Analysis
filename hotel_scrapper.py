import urllib
import json
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://www.tripadvisor.in/Hotels-g304554-Mumbai_Maharashtra-Hotels.html"
html_doc = urllib.request.urlopen(URL)

soup = BeautifulSoup(html_doc, 'html.parser')

for x in soup.find_all():
	if "data-hotels-data" in x.attrs:
		Dict = x["data-hotels-data"]


Dict = json.loads(Dict)

D = []

# Check the price

for hotel in Dict["hotels"]:
	D.append({'Name':hotel['name'], 'Latitude':hotel['geoPoint']['latitude'], 'Longitude':hotel['geoPoint']['longitude'], 'Price':hotel['offers'][0]['price']})

df = pd.DataFrame(D)

df.to_csv("hotels.csv", index=False)