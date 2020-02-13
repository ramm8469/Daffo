# Here in this file, we are going to see the demo of decorator in Python

# Before undersating decorator, first let's understand closure in Python

def Outer_function():
    message = "Hello World"
    def Inner_function():
        print(message)
    return Inner_function

data = Outer_function()
data()
data()
data()

# So, Closure is just when an inner function has access to the 
# variables of outer function or the scope in which it is defined
# even after the outer function has been executed

# Now, based on closure, let's understand Decorator in Python

# Function Based Decorators

def decorator_function(original_function):
    def wrapper_function():
        print("The wrapper function is executed before the {}".format(original_function.__name__))
        return original_function()
    return wrapper_function


# Now, lets make a display function to which we want to decorate

# Now, Let's decorate it in Pythonic Faishon
# @decorator_function
def display():
    print("This is from the display function")

# After decorating call the display() function

display()
display()

# # # Now, let's decorate it...in traditional fashion
# display_var = decorator_function(display)

# display_var()
# display()
# display_var()

# Thus : Decorator is a design pattern in python, which allows us
# to use the property of function as a first class citizen in Python
# (I.E: we can pass function as an argument, we can return function
# as a return value and so on...), and without updating the original
# function code, add new functionality to it


# Class Based Decorators

class DecoratorClass:
    def __init__(self,original_function):
        self.original_function = original_function
    
    # The Wrapper function can be seen as
    def __call__(self):
        print("This is from the call method executed before {}".format(self.original_function.__name__))
        return self.original_function()
    

print("*"*50)

# Now, create another display function
@DecoratorClass
def myDisplay():
    print("This is from my Display")

myDisplay()