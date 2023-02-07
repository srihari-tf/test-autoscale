import requests

import time
import requests
import datetime
import concurrent.futures
import os

url = os.environ["URL"]
MAX_THREADS = 10
CONCURRENT_THREADS = 10

def send_api_request():
    while True:
        print ('Sending API request: ', url)
        r = requests.get(url)
        print ('Received: ', r.status_code, r.text)

start_time = datetime.datetime.now()
print ('Starting:', start_time)

with concurrent.futures.ThreadPoolExecutor(MAX_THREADS) as executor:
    futures = [ executor.submit(send_api_request) for x in range (CONCURRENT_THREADS) ]
time.sleep(5)
end_time = datetime.datetime.now()
print ('Finished start time:', start_time, 'duration: ', end_time-start_time)