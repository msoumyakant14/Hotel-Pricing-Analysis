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
		Amenities = {'Air conditioning':0, 'Housekeeping':0, 'Private balcony':0, 'Private bathrooms':0, 'VIP room facilities':0, 'Complimentary toiletries':0, 'Room service':0, 'Telephone':0, 'Minibar':0, 'Flatscreen TV':0, 'Wifi':0, 'Pool':0, 'Bar / lounge':0, 'Poolside bar':0, 'Free parking':0, 'Breakfast':0, 'Restaurant':0, 'Airport transportation':0, 'Car hire':0, 'Taxi service':0, 'Banquet room':0, 'Meeting rooms':0, 'Conference facilities':0, 'Spa':0, 'Sauna':0, 'Currency exchange':0, '24-hour security':0, 'Concierge':0, 'Baggage storage':0, 'Sun terrace':0, 'Shops':0, 'Butler service':0, 'First aid kit':0, 'Infirmary':0, '24-hour front desk':0, 'Private check-in / check-out':0, 'Express check-in / check-out':0, 'Dry cleaning':0, 'Laundry service':0, 'Shoeshine':0, 'Ocean view':0, 'City view':0, 'Landmark view':0, 'Pool view':0, 'Non-smoking rooms':0, 'Smoking rooms available':0, 'Suites':0}
		print(hotel['name'])
		detailsURL = BaseURL + hotel['detailUrl']
		detailsDoc = urllib.request.urlopen(detailsURL)
		soup = BeautifulSoup(detailsDoc, 'html.parser')
		rating = soup.find("span", {"class": "_3cjYfwwQ"}).text
		print(rating)
		reviews = soup.find("span", {"class": "_3jEYFo-z"}).text.split()[0]
		print(reviews)
		amenities = soup.find_all("div", {"class": "_2rdvbNSg"})
		#amenities_set = set([])
		for a in amenities:
			#amenities_set.add(a.text)
			Amenities[a.text]=1
		D.append({'Name':hotel['name'], 'Latitude':hotel['geoPoint']['latitude'], 'Longitude':hotel['geoPoint']['longitude'], 'Air conditioning':Amenities['Air conditioning'], 'Housekeeping':Amenities['Housekeeping'], 'Private balcony':Amenities['Private balcony'], 'Private bathrooms':Amenities['Private bathrooms'], 'VIP room facilities':Amenities['VIP room facilities'], 'Complimentary toiletries':Amenities['Complimentary toiletries'], 'Room service':Amenities['Room service'], 'Telephone':Amenities['Telephone'], 'Minibar':Amenities['Minibar'], 'Flatscreen TV':Amenities['Flatscreen TV'], 'Wifi':Amenities['Wifi'], 'Pool':Amenities['Pool'], 'Bar / lounge':Amenities['Bar / lounge'], 'Poolside bar':Amenities['Poolside bar'], 'Free parking':Amenities['Free parking'], 'Breakfast':Amenities['Breakfast'], 'Restaurant':Amenities['Restaurant'], 'Airport transportation':Amenities['Airport transportation'], 'Car hire':Amenities['Car hire'], 'Taxi service':Amenities['Taxi service'], 'Banquet room':Amenities['Banquet room'], 'Meeting rooms':Amenities['Meeting rooms'], 'Conference facilities':Amenities['Conference facilities'], 'Spa':Amenities['Spa'], 'Sauna':Amenities['Sauna'], 'Currency exchange':Amenities['Currency exchange'], '24-hour security':Amenities['24-hour security'], 'Concierge':Amenities['Concierge'], 'Baggage storage':Amenities['Baggage storage'], 'Sun terrace':Amenities['Sun terrace'], 'Shops':Amenities['Shops'], 'Butler service':Amenities['Butler service'], 'First aid kit':Amenities['First aid kit'], 'Infirmary':Amenities['Infirmary'], '24-hour front desk':Amenities['24-hour front desk'], 'Private check-in / check-out':Amenities['Private check-in / check-out'], 'Express check-in / check-out':Amenities['Express check-in / check-out'], 'Dry cleaning':Amenities['Dry cleaning'], 'Laundry service':Amenities['Laundry service'], 'Shoeshine':Amenities['Shoeshine'], 'Ocean view':Amenities['Ocean view'], 'City view':Amenities['City view'], 'Landmark view':Amenities['Landmark view'], 'Pool view':Amenities['Pool view'], 'Non-smoking rooms':Amenities['Non-smoking rooms'], 'Smoking rooms available':Amenities['Smoking rooms available'], 'Suites':Amenities['Suites'], 'Rating':rating, 'Number of reviews':reviews, 'Price':hotel['offers'][0]['price']})
		time.sleep(random.randint(1,5))

	print("Page",pages+1,"completed.")

df = pd.DataFrame(D)

df.to_csv("hotels.csv", index=False)