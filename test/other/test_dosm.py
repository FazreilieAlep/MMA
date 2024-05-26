import requests
import pprint

url = "https://api.data.gov.my/data-catalogue?id=hies_malaysia_percentile&limit=3" 

response_json = requests.get(url=url).json()
pprint.pprint(response_json)
