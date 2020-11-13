import random
import urllib
import time
import json
from bs4 import BeautifulSoup
import pandas as pd

BaseURL = "https://www.tripadvisor.in"
URL = BaseURL + "/Hotels-g304554-Mumbai_Maharashtra-Hotels.html"

D = []

f = open("hotel_backup.csv", "w")
f.write('Name,Latitude,Longitude,Air conditioning,Housekeeping,Private balcony,Private bathrooms,VIP room facilities,Complimentary toiletries,Room service,Telephone,Minibar,Flatscreen TV,Wifi,Pool,Bar / lounge,Poolside bar,Free parking,Breakfast available,Restaurant,Airport transportation,Car hire,Taxi service,Banquet room,Meeting rooms,Conference facilities,Spa,Sauna,Currency exchange,24-hour security,Concierge,Baggage storage,Sun terrace,Shops,Butler service,First aid kit,Infirmary,24-hour front desk,Private check-in / check-out,Express check-in / check-out,Dry cleaning,Laundry service,Shoeshine,Ocean view,City view,Landmark view,Pool view,Non-smoking rooms,Smoking rooms available,Suites,Rating,Number of reviews,Price\n')
for pages in range(40):
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
		time.sleep(random.randint(3,5))
		try:
			Amenities = {'Air conditioning':0, 'Housekeeping':0, 'Private balcony':0, 'Private bathrooms':0, 'VIP room facilities':0, 'Complimentary toiletries':0, 'Room service':0, 'Telephone':0, 'Minibar':0, 'Flatscreen TV':0, 'Wifi':0, 'Pool':0, 'Bar / lounge':0, 'Poolside bar':0, 'Free parking':0, 'Breakfast available':0, 'Restaurant':0, 'Airport transportation':0, 'Car hire':0, 'Taxi service':0, 'Banquet room':0, 'Meeting rooms':0, 'Conference facilities':0, 'Spa':0, 'Sauna':0, 'Currency exchange':0, '24-hour security':0, 'Concierge':0, 'Baggage storage':0, 'Sun terrace':0, 'Shops':0, 'Butler service':0, 'First aid kit':0, 'Infirmary':0, '24-hour front desk':0, 'Private check-in / check-out':0, 'Express check-in / check-out':0, 'Dry cleaning':0, 'Laundry service':0, 'Shoeshine':0, 'Ocean view':0, 'City view':0, 'Landmark view':0, 'Pool view':0, 'Non-smoking rooms':0, 'Smoking rooms available':0, 'Suites':0}
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
			if (hotel['geoPoint']['latitude']!=0 or hotel['geoPoint']['latitude']!=0.0)  and (hotel['geoPoint']['longitude']!=0 or hotel['geoPoint']['longitude']!=0.0):
				D.append({'Name':hotel['name'], 'Latitude':hotel['geoPoint']['latitude'], 'Longitude':hotel['geoPoint']['longitude'], 'Air conditioning':Amenities['Air conditioning'], 'Housekeeping':Amenities['Housekeeping'], 'Private balcony':Amenities['Private balcony'], 'Private bathrooms':Amenities['Private bathrooms'], 'VIP room facilities':Amenities['VIP room facilities'], 'Complimentary toiletries':Amenities['Complimentary toiletries'], 'Room service':Amenities['Room service'], 'Telephone':Amenities['Telephone'], 'Minibar':Amenities['Minibar'], 'Flatscreen TV':Amenities['Flatscreen TV'], 'Wifi':Amenities['Wifi'], 'Pool':Amenities['Pool'], 'Bar / lounge':Amenities['Bar / lounge'], 'Poolside bar':Amenities['Poolside bar'], 'Free parking':Amenities['Free parking'], 'Breakfast available':Amenities['Breakfast available'], 'Restaurant':Amenities['Restaurant'], 'Airport transportation':Amenities['Airport transportation'], 'Car hire':Amenities['Car hire'], 'Taxi service':Amenities['Taxi service'], 'Banquet room':Amenities['Banquet room'], 'Meeting rooms':Amenities['Meeting rooms'], 'Conference facilities':Amenities['Conference facilities'], 'Spa':Amenities['Spa'], 'Sauna':Amenities['Sauna'], 'Currency exchange':Amenities['Currency exchange'], '24-hour security':Amenities['24-hour security'], 'Concierge':Amenities['Concierge'], 'Baggage storage':Amenities['Baggage storage'], 'Sun terrace':Amenities['Sun terrace'], 'Shops':Amenities['Shops'], 'Butler service':Amenities['Butler service'], 'First aid kit':Amenities['First aid kit'], 'Infirmary':Amenities['Infirmary'], '24-hour front desk':Amenities['24-hour front desk'], 'Private check-in / check-out':Amenities['Private check-in / check-out'], 'Express check-in / check-out':Amenities['Express check-in / check-out'], 'Dry cleaning':Amenities['Dry cleaning'], 'Laundry service':Amenities['Laundry service'], 'Shoeshine':Amenities['Shoeshine'], 'Ocean view':Amenities['Ocean view'], 'City view':Amenities['City view'], 'Landmark view':Amenities['Landmark view'], 'Pool view':Amenities['Pool view'], 'Non-smoking rooms':Amenities['Non-smoking rooms'], 'Smoking rooms available':Amenities['Smoking rooms available'], 'Suites':Amenities['Suites'], 'Rating':rating, 'Number of reviews':reviews, 'Price':hotel['offers'][0]['price']})
				f.write(hotel['name'] + ',' + str(hotel['geoPoint']['latitude']) + ',' + str(hotel['geoPoint']['longitude']) + ',' + str(Amenities['Air conditioning']) + ',' + str(Amenities['Housekeeping']) + ',' + str(Amenities['Private balcony']) + ',' + str(Amenities['Private bathrooms']) + ',' + str(Amenities['VIP room facilities']) + ',' + str(Amenities['Complimentary toiletries']) + ',' + str(Amenities['Room service']) + ',' + str(Amenities['Telephone']) + ',' + str(Amenities['Minibar']) + ',' + str(Amenities['Flatscreen TV']) + ',' + str(Amenities['Wifi']) + ',' + str(Amenities['Pool']) + ',' + str(Amenities['Bar / lounge']) + ',' + str(Amenities['Poolside bar']) + ',' + str(Amenities['Free parking']) + ',' + str(Amenities['Breakfast available']) + ',' + str(Amenities['Restaurant']) + ',' + str(Amenities['Airport transportation']) + ',' + str(Amenities['Car hire']) + ',' + str(Amenities['Taxi service']) + ',' + str(Amenities['Banquet room']) + ',' + str(Amenities['Meeting rooms']) + ',' + str(Amenities['Conference facilities']) + ',' + str(Amenities['Spa']) + ',' + str(Amenities['Sauna']) + ',' + str(Amenities['Currency exchange']) + ',' + str(Amenities['24-hour security']) + ',' + str(Amenities['Concierge']) + ',' + str(Amenities['Baggage storage']) + ',' + str(Amenities['Sun terrace']) + ',' + str(Amenities['Shops']) + ',' + str(Amenities['Butler service']) + ',' + str(Amenities['First aid kit']) + ',' + str(Amenities['Infirmary']) + ',' + str(Amenities['24-hour front desk']) + ',' + str(Amenities['Private check-in / check-out']) + ',' + str(Amenities['Express check-in / check-out']) + ',' + str(Amenities['Dry cleaning']) + ',' + str(Amenities['Laundry service']) + ',' + str(Amenities['Shoeshine']) + ',' + str(Amenities['Ocean view']) + ',' + str(Amenities['City view']) + ',' + str(Amenities['Landmark view']) + ',' + str(Amenities['Pool view']) + ',' + str(Amenities['Non-smoking rooms']) + ',' + str(Amenities['Smoking rooms available']) + ',' + str(Amenities['Suites']) + ',' + str(rating) + ',' + str(reviews) + ',' + str(hotel['offers'][0]['price']) + '\n')
		except:
			pass

	print("Page",pages+1,"completed.")


df = pd.DataFrame(D)

df = df.dropna()

df.to_csv("hotels.csv", index=False)