# Here in this file we are going to see the demo of the Dictionary Data Structure
# available in Python.
# Dictionary is a key-value paired data structure in python
# In other Programming languages, we can see Dicitionary as HashMap
# Dictionary is an unordered, mutable data structure
# we can create dicitonary by two ways

# 1 : by  using curly braces for a variable/reference
print("*"*50)
cars = {
    'Honda' : 2,
    'BMW' : 1,
    'Audi' : 3,
    'Mercedes' : 4,
    'Rolls'  : 1
}

print(cars)

# 2  : by using dict() constructor
print("*"*50)
new_cars  = dict(
    Honda = 1,
    BMW  =2,
    Mercedes = 3,
    Audi = 4,
    Rolls = 5
)

print(new_cars)


# Operations/Methods on Dictionary
print("*"*50)

# to add a new key-valued pair in the dictionary
new_cars['Suzuki'] = 6
print(new_cars)

# to remove a key-valued pair from the dictionary
print("*"*50)
removed = new_cars.pop('Suzuki') # we get the value of removed element as return
print(removed)
print(new_cars)

# to update a value of a key in the dictonary
new_cars['Rolls']  = 4
print("*"*50)
print(new_cars)

# another way of updating the value using key
print("*"*50)
new_cars.update(Rolls = 6)
print(new_cars)

# Getting all the values of the dictionary
values  = new_cars.values()
print("*"*50)
print(values)

# Getting all the keys of the dictionary
keys =  new_cars.keys()
print("*"*50)
print(keys)

