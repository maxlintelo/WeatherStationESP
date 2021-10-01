import requests
import random
import time
import datetime

API_URL = "http://81.207.176.52:8081/api/v1"

def main():
    print('Filling...')
    while(1):
        obj = {
            'temperature': random.uniform(-20, 40),
            'humidity': random.uniform(0, 100)
        }
        r = requests.post(API_URL, data=obj)
        print(datetime.datetime.now().strftime("[DATE] %I:%M:%S%p on %B %d, %Y") + "\n[RES] " + r.text)
        time.sleep(5)

if __name__ == "__main__":
    main()
