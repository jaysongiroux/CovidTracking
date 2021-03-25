import time
import os
import requests
import json

# https://api.covidtracking.com/v1/states/daily.json
data = requests.get("https://api.covidtracking.com/v1/states/daily.json")

try:
    os.makedirs("../Data/Daily")
except OSError as e:
    print("Folder Exists Moving on...")

fileName = time.strftime("%Y%m%d-%H%M%S") + ".json"
with open("../Data/Daily/" + fileName, 'w') as output_file:
    print("Writing: ", fileName , ".json")
    json.dump(data.json(), output_file, indent=3)
