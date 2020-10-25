import re
import json
import requests
import pandas as pd
import sys

# url_base = "https://www.tripadvisor.in/Attractions-g304558-Activities-a_allAttractions.true-Kolkata_Calcutta_Kolkata_District_West_Bengal.html"
url_base=sys.argv[2]
# url2 ="https://www.tripadvisor.in/Attractions-g304554-Activities-a_allAttractions.true-Mumbai_Maharashtra.html"
url_parts=url_base.split('-a_')
total_page_count=int(sys.argv[1])
df_list = []
for i in range(total_page_count):
	url_final=url_parts[0]+'-oa'+str(i*30)+'-a_'+url_parts[1]
	html_text = requests.get(url_final).text

	data_upper = re.search(r'window\.__WEB_CONTEXT__=(.*?});', html_text).group(1)
	data_upper = data_upper.replace('pageManifest', '"pageManifest"')
	data_final = re.search(r'"attractionsResponse":.*?"totalResults":.*?}', data_upper).group(0)
	data_final = data_final.replace('"attractionsResponse":[', '')

	final_json = json.loads(data_final)

	category_dict= {55:"Boat Tours and Water Sports",
					53:"Casinos and Gambling",
					41:"Classes and Workshops",
					58:"Concerts and Shows",
					36:"Food and Drink",
					56:"Fun and Games",
					49:"Museums",
					57:"Nature and Parks",
					20:"Nightlife",
					61:"Outdoor Activities",
					26:"Shopping",
					47:"Sights and Landmarks",
					40:"Spas and Wellness",
					42:"Tours",
					59:"Transportation",
					60:"Traveller Resources",
					52:"Water and Amusement Parks",
					48:"Zoos and Aquariums",
					51:"Other"}




	for attraction in final_json["attractions"]:
		intermediate_list=[attraction["name"],attraction["latitude"],attraction["longitude"],attraction["reviewCount"],attraction["reviewScore"]]
		category_id_string=''
		category_type_string=''
		# category_ids=[]
		# category_type=[]
		for i in attraction["categoryIds"]:
			if category_type_string!='':
				category_type_string=category_type_string+';'+category_dict[i]
			else:
				category_type_string=category_dict[i]

			if category_id_string!='':
				category_id_string=category_id_string+';'+str(i)
			else:
				category_id_string=str(i)

			# change to strings (; separated values)
			#category_type.append(category_dict[i])


		intermediate_list.append(category_id_string)
		intermediate_list.append(category_type_string)
		df_list.append(intermediate_list)

df = pd.DataFrame(df_list, columns = ['Name', 'Latitude','Longitude','Review Count','Review Score','Category Id', 'Category Type'])

df.to_csv('attractions.csv',index=False)




