import requests
import sys
import json #library to manipulate json formats

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

#print(json.dumps(response.json(), indent=2))#print the response in json format

o = response.json()
for result in o["results"]:#search on the json, on the results the field call trackname
    print(result["trackName"])
