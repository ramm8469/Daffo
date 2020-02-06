# Here in this file we are going to see the functions demo : How to write 
# Functions in python

# We Define and Declare a function in python using the keyword "define"

# defining a simple function
def simpleFunction():
    print("This is a simple function")

# we can invoke/activate a function by calling it with it's name

simpleFunction()

# We can have functions with arguments/parameter and we do also have value/values
# returned by a function

# Demo of a function with args and return value

def square(nums):
    return nums**2

print("="*50)
# calling the function
print(square(2))
print(square(4))

