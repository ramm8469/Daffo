# Here in this file, we are going to see the exception handling with a
# simple demo/example with "raise" keyword to force an explict exception 
# raise while executing...

try:
    res = 5/0 # Zero Division error
    raise NameError("Hi, this is a name error")
except ZeroDivisionError:
    print("Can not divide By 0")
except NameError:
    print("There is a Name Error")
except:
    print(" An error occured, this message is from generic exception handling")
finally:
    print("This is from the finally Block")