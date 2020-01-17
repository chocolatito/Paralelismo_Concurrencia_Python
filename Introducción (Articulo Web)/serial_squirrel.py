# serial_squirrel.py

from websites import WEBSITE_LIST
from utils import check_website
import time


start_time = time.time()

for address in WEBSITE_LIST:
    check_website(address)

end_time = time.time()

print("Time for SerialSquirrel: %ssecs" % (end_time - start_time))

# WARNING:root:Timeout expired for
# website http://really-cool-available-domain.com
# WARNING:root:Timeout expired for
# website http://another-really-interesting-domain.co
# WARNING:root:Website http://bing.com returned status_code=405
# Time for SerialSquirrel: 15.881232261657715secs
