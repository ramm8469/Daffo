# list is a data structure in python which can store any kind of data
# list is mutable and ordered
# we can define list using [] - square brackets or by using list() constructor
# In other programming languages like C++ or Java, We call it Array

print('*'*50)
# Creating Normal List
myList = [1,2,3,4,5]
print(myList)

print('*'*50)
# Creating List using the List() Constructor

myData = list((1,2,3,4,5))
print(myData)

# Some Offently used method of list

# to add a new element to the list
myData.append("this is a new data")
print("*"*50)
print(myData)

# to remove a element from the list
print("*"*50)
removed_ele = myData.pop()
print(myData)

# to get the size of the list
print("*"*50)
print("Length of the list : ")
print(len(myData))


