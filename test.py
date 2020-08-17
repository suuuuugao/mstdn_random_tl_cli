import os
import requests
import random
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
token_key = os.environ.get("TOKEN_KEY")
auth = "Bearer " + token_key

resp = requests.get(
    "https://muknown.jp/api/v1/timelines/home?limit=30",
    headers={
        "Authorization": auth,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
    },
)

for status in resp.json():
    if random.randint(0,1):
        print(status["content"])
