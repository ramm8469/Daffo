# Here in This file we are going to see the demo on Strings
str  = "Hello World !"

print(str)

# string slicing....
# String slicing is a way of slicing out substring out of a given string
# String slicing can be perfromed by two ways:
# Using the list access types : Like str[start,end,step_size]

print("=========Slicing with list like access [start,end,step_size]===========")

print(str[0:5]) # Hello

print(str[-1:-8:-1]) # ! dlroW // Negative Slicing
# Note : Whenever we are going to do a negative slicing on string,
# Make sure that the step size shoul also be in negative

# Using the slice() method with the string reference

print("*"*50)
print("=========Slicing with slice() built in funciton===========")
sub_str = slice(0,5)
print(str[sub_str]) # Hello

sub_str1 = slice(-1,-8,-1)
print(str[sub_str1])



