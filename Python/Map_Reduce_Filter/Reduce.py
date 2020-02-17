# Use of lambda() with reduce()

# The reduce() function in Python takes in a function and a list as argument.
#  The function is called with a lambda function and a list and a new reduced 
#  result is returned. This performs a repetitive operation over the pairs of 
#  the list. This is a part of functools module. Example:
# filter_none


# Python code to illustrate  
# reduce() with lambda() 
# to get sum of a list 
from functools import reduce
li = [5, 8, 10, 20, 50, 100] 
sum = reduce((lambda x, y: x + y), li) 
print (sum) 
