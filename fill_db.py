import requests
import random
import time
import datetime

API_URL = "http://81.207.176.52:8081/api/"

def old_post():
    obj = {
        'temperature': random.uniform(-20, 40),
        'humidity': random.uniform(0, 100),
        'pressure': random.uniform(960, 1060),
    }
    r = requests.post(API_URL + "v2", data=obj)
    print(datetime.datetime.now().strftime("[DATE] %I:%M:%S%p on %B %d, %Y") + "\n[RES] " + r.text)

def new_post():
    temperature = str(random.uniform(-20, 40))
    humidity = str(random.uniform(0, 100))
    pressure = str(random.uniform(960, 1060))
    r = requests.get(API_URL + "mock/post?temperature=" + temperature + "&humidity=" + humidity + "&pressure=" + pressure, data=None)
    print(datetime.datetime.now().strftime("[DATE] %I:%M:%S%p on %B %d, %Y") + "\n[RES] " + r.text)


def main():
    print('Filling...')
    while(1):
        new_post()
        time.sleep(10)
        

if __name__ == "__main__":
    main()
