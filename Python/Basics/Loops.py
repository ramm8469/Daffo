# In this file we are going to see the different loops available in Python
# and Operations on it

myList = list(range(11))
print(myList,end="-")
print()
# While Loop
length = len(myList)
i = 0
while(i < length):
    print(myList[i],end="-")
    i += 1

print()

# For Loop

for i in myList:
    print(i,end="==")
print()