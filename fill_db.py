import requests
import random

API_URL = "http://81.207.176.52:8081/api/v1"

def main():
    print('Filling...')
    for x in range(1000):
        obj = {
            'temperature': random.randrange(-20, 40),
            'humidity': random.randrange(0, 100)
        }
        r = requests.post(API_URL, data=obj)
        print(str(x) + r.text)

if __name__ == "__main__":
    main()
