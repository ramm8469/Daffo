# Here in this file we are going to see the time module available 
# in Python

#Importing the time module
import time


# Getting the current local time
localtime = time.localtime(time.time())
print ("Local current time :" ,localtime[2],"/",localtime[1],"/",localtime[0])
print("Hours : Minutes : Seconds  === ",localtime[3],":",localtime[4],":",localtime[5])

