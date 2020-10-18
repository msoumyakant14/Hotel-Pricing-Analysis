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
		print(hotel['name'])
		detailsURL = BaseURL + hotel['detailUrl']
		detailsDoc = urllib.request.urlopen(detailsURL)
		soup = BeautifulSoup(detailsDoc, 'html.parser')
		rating = soup.find("span", {"class": "_3cjYfwwQ"}).text
		print(rating)
		reviews = soup.find("span", {"class": "_3jEYFo-z"}).text.split()[0]
		print(reviews)
		amenities = soup.find_all("div", {"class": "_2rdvbNSg"})
		amenities_set = set([])
		for a in amenities:
			amenities_set.add(a.text)
		if 'Air conditioning' in amenities_set:
			AC = 1
		else:
			AC = 0
		if 'Room service' in amenities_set:
			RS = 1
		else:
			RS = 0
		D.append({'Name':hotel['name'], 'Latitude':hotel['geoPoint']['latitude'], 'Longitude':hotel['geoPoint']['longitude'], 'Room service available':RS, 'AC rooms':AC, 'Rating':rating, 'Number of reviews':reviews, 'Price':hotel['offers'][0]['price']})
		time.sleep(random.randint(1,5))

	print("Page",pages+1,"completed.")

df = pd.DataFrame(D)

df.to_csv("hotels.csv", index=False)