import random
import urllib
import time
import json
from bs4 import BeautifulSoup
import pandas as pd

BaseURL = "https://www.tripadvisor.in"
URL = BaseURL + "/Hotels-g304554-Mumbai_Maharashtra-Hotels.html"

D = []

for pages in range(2):
	time.sleep(5)
	html_doc = urllib.request.urlopen(URL)

	soup = BeautifulSoup(html_doc, 'html.parser')

	for x in soup.find_all():
		if "data-hotels-data" in x.attrs:
			Dict = x["data-hotels-data"]


	pagination = soup.find("a", {"class": "nav next ui_button primary cx_brand_refresh_phase2"})
	URL = BaseURL + pagination['href']


	Dict = json.loads(Dict)

	# Check the price

	for hotel in Dict["hotels"]:
		detailsURL = BaseURL + hotel['detailUrl']
		detailsDoc = urllib.request.urlopen(detailsURL)
		soup = BeautifulSoup(detailsDoc, 'html.parser')
		rating = soup.find("span", {"class": "_3cjYfwwQ"}).text
		print(rating)
		D.append({'Name':hotel['name'], 'Latitude':hotel['geoPoint']['latitude'], 'Longitude':hotel['geoPoint']['longitude'], 'Rating':rating, 'Price':hotel['offers'][0]['price']})
		time.sleep(random.randint(1,5))

	print("Page",pages+1,"completed.")

df = pd.DataFrame(D)

df.to_csv("hotels.csv", index=False)