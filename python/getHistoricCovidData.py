import requests
import json
import os

try:
    os.makedirs("../Data/Historic")
except OSError as e:
    print("Folder Exists Moving on...")

states = ["AK", "AL", "AR", "AZ", "CA", "CO", "CT", "DC",
    "DE", "FL", "GA", "HI", "IA", "ID", "IL", "IN", "KS", "KY", "LA",
    "MA", "MD", "ME", "MI", "MN", "MO", "MS", "MT", "NC", "ND", "NE",
    "NH", "NJ", "NM", "NV", "NY", "OH", "OK", "OR", "PA", "RI", "SC",
    "SD", "TN", "TX", "UT", "VA", "VT", "WA", "WI", "WV", "WY"]

for state in states:
    # API Website:
    # https: // api.covidtracking.com / v1 / states / ca / daily.json
    # Will need to download all public data from this site due to API being depreciated in may 2021
    data = requests.get("https://api.covidtracking.com/v1/states/" + state.lower() + "/daily.json")

    with open("../Data/Historic/" + state + ".json", 'w') as output_file:
        print("Writing: ", state, ".json")
        json.dump(data.json(), output_file, indent=3)

print("Completed")