# As we already know that def keyword is used to define the normal
#  functions and the lambda keyword is used to create anonymous functions. 
# It has the following syntax:
# lambda arguments: expression
#  This function can have any number of arguments but only one expression, which is evaluated and returned.
#     One is free to use lambda functions wherever function objects are required.
#     You need to keep in your knowledge that lambda functions are syntactically restricted to a single expression.
#     It has various uses in particular fields of programming besides other types of expressions in functions.

   
# Example : 
def cube(digit):
    return digit*digit*digit


cube_lambda = lambda digit : digit*digit*digit

# calling both, Lambda and Non-lambda functions

print(cube(3))
print(cube_lambda(3))