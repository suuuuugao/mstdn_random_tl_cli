import requests
import json

url = 'https://muknown.jp'

res = requests.get(url)

lists = json.loads(res.text)

for list in lists:
    print(list['name'] + ':' + list['alpha2Code'])