import json

import requests

url = "https://api.agify.io?name=Matt"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
