# Here in this file, we are going to see the exception handling with a
# simple demo/example which handles multiple exception

# Note : If a exception is not falls in any specific excpetion categories
# mentioned explicitly, then it goes to the generic exception

try:
    res = 5/0 # Zero Division error
except ZeroDivisionError:
    print("You can not divide a number by Zero")
except:
    print(" An error occured, this message is from generic exception handling")
finally:
    print("This is from the finally Block")