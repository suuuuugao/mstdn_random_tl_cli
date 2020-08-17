import requests

url = 'https://muknown.jp'
restapi = requests.get(url)
print(restapi.ok)

#result
#llllll:study_log (^-^)$ python3 rest_api_check.py
#True