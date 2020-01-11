# future_squirrel.py
from websites import WEBSITE_LIST
from utils import check_website
import time
import concurrent.futures as c_futures

NUM_WORKERS = 4

start_time = time.time()

with c_futures.ThreadPoolExecutor(max_workers=NUM_WORKERS) as executor:
    futures = {
        executor.submit(check_website, address) for address in WEBSITE_LIST}
    c_futures.wait(futures)

end_time = time.time()

print("Time for FutureSquirrel: %ssecs" % (end_time - start_time))

# WARNING:root:Timeout expired for
# website http://really-cool-available-domain.com
# WARNING:root:Timeout expired for
# website http://another-really-interesting-domain.co
# WARNING:root:Website http://bing.com returned status_code=405
# Time for FutureSquirrel: 1.812899112701416secs
