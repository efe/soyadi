import requests
import json
from bs4 import BeautifulSoup

url = "https://www.tbmm.gov.tr/develop/owa/milletvekillerimiz_sd.liste"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

all_tr_elements = soup.find_all("tr")

parties = ['AK Parti', 'CHP', 'MHP', 'İYİ Parti', 'HDP', 'DP', 'BBP', 'BAĞIMSIZ', 'TİP', 'Saadet P']
parliamentarians = []

for tr_element in all_tr_elements:
	full_name = tr_element.contents[1].text
	party = tr_element.contents[5].text

	if party in parties:
		obj = {
			"last_name": full_name.split()[-1],
			"party": party
		}
		parliamentarians.append(obj)

with open('parliamentarians.json', 'w') as f:
	json.dump(parliamentarians, f)
