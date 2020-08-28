import os
import requests
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
token_key = os.environ.get("TOKEN_KEY")
auth = "Bearer " + token_key
url = "https://muknown.jp/api/v1/timelines/home?limit=30"

def req_func():
    return requests.get(
        url,
        headers={
            "Authorization": auth,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
        },
    )

