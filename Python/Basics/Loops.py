# In this file we are going to see the different loops available in Python
# and Operations on it

myList = list(range(11))
print(myList)
# While Loop
length = len(myList)
while(length > 0):
    print(myList[length],end="-")
    length = length-1

# For Loop