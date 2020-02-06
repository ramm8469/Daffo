# Here in this file we are going to see the Set data structure 
# Available in the Python
# Sets are unordered collections of unique elements

# we can declare sets by two ways :

# 1 : by using the {} curly braces
mySet  = {1,2,3,3,4,5,66,7,66,7}
print("*"*50)
print(mySet) # Note down that the duplicate elements are automatically eleminated




# 2 : by using the set() constructor
myNewSet  = set((1,2,3,3,4,5,66,7,66,7))
print("*"*50)
print(mySet)


# Note :  Creating an empty set using {} curly braces results in creating
# an empty dictionary by default

# example ...
set_emp = {}
set_emp_1 = set()
print(type(set_emp)) # class :  dict
print(type(set_emp_1)) # class  : set

# Operations/Methods performed 
# sets are define 
print("*"*50)
print("=========Sets Operations==============")
A = {0, 2, 4, 6, 8}
B = {1, 2, 3, 4, 5} 
  
# union 
print("Union :", A | B) 
  
# intersection 
print("Intersection :", A & B) 
  
# difference 
print("Difference :", A - B) 
  
# symmetric difference 
print("Symmetric difference :", A ^ B) 

