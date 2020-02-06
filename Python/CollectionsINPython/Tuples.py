# Here in this file we are going to see the Tuple data structure available
# in the Python
# Tuple is an ordered Collection of elements
# Tuples are immutable in nature. : I.e: Once it is declared, it's value can't
# be changed later

# Creating Tuple
# we can create Tuple by two ways:-
# 1 :  By Using paranthesis for a variable

print("*"*50)
my_tuple = ("data",1,2,3,4.0,True)
print(my_tuple)

# 2 :  By Using the Tuple() Constructor
print("*"*50)
my_tuple1 = tuple(("data",1,2,3,4.0,True))
print(my_tuple1)

# Accessing the tuple elements
print("*"*50)
d1 = my_tuple1[0]
d2 = my_tuple1[1]

print(d1," : ",d2)

# Modifying the tuple
# my_tuple1[0] = True # This gives an eror : TypeError
# print(my_tuple1)



