import random

def random_func():
    for status in resp.json():
        if random.randint(0, 1):
            print(status["account"]["username"])
            print(status["content"])
