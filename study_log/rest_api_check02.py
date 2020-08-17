import requests

url = 'https://muknown.jp/api/v1/instance'
restapi = requests.get(url)
print(restapi.ok)
