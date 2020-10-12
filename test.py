import urllib
import json
from bs4 import BeautifulSoup
import pandas as pd

URL = "/Hotel_Review-g304554-d307116-Reviews-Grand_Hyatt_Mumbai_Hotel_Residences-Mumbai_Maharashtra.html"

URL = "https://www.tripadvisor.in" + URL

html_doc = urllib.request.urlopen(URL)

soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())






