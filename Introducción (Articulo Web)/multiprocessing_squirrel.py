# multiprocessing_squirrel.py
from websites import WEBSITE_LIST
from utils import check_website
import time
import socket
import multiprocessing


if __name__ == '__main__':

    NUM_WORKERS = 4

    start_time = time.time()

    with multiprocessing.Pool(processes=NUM_WORKERS) as pool:
        results = pool.map_async(check_website, WEBSITE_LIST)
        results.wait()

    end_time = time.time()

    print("Time for MultiProcessingSquirrel: %ssecs" % (end_time - start_time))

    # WARNING:root:Timeout expired for
    # website http://really-cool-available-domain.com
    # WARNING:root:Timeout expired for
    # website http://another-really-interesting-domain.co
    # WARNING:root:Website http://bing.com returned status_code=405
    # Time for MultiProcessingSquirrel: 2.8224599361419678secs
