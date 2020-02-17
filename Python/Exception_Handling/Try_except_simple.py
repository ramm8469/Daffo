# Here in this file, we are going to see the exception handling with a
# simple demo/example

try:
    res = 5/5 # Zero Division error
except:
    print(" An error occured, this message is from generic exception handling")
# Note  : The Else block will executes only when the try block does not
# Through an exception,I.e: If Try blocks executes successfully then,
# the else block will also executes, Otherwise except block will executes
else:
    print("This is from else block")

finally:
    print("This is from the finally Block")
