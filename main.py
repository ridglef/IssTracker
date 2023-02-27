import requests
import json
import time

def track():
    base = "https://api.wheretheiss.at/v1/satellites/25544"
    response = requests.get(base)
    jsondata = json.loads(response.text)
    latt = jsondata["latitude"]
    long = jsondata["longitude"]
    print(f"The Iss is at {latt}, {long}")
    time.sleep(8)
    track()
track()
