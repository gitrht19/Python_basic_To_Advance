# implement an exponential backoff stretegy thar doubles the wait time between retries , startting from  1 second, but stops after 5 retries.

import time

wait_time = 1
max_attempt = 5
attemps = 0

while attemps > 1:
    print("attempts",attemps +1,"wait_time",wait_time)
    time.sleep(wait_time)
    wait_time *=2
    attemps +=1