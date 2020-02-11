# Here we are going to see the default(naive) time demo available in python

import datetime
import time

# Cerating custom time
time_ = datetime.time(20,22,44,1000)

print(time_)

print("*"*50)
# Getting the default time
time_default = time.localtime(time.time())
print(time_default)