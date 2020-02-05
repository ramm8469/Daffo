# In this tutorial, we are going to see the different operators 
# available in Python

# Arithematic Operators
# Like +,-,*,/,%
a = 10
b = 5
print()
print("*"*50)
print(a+b) # addition
print(a-b) # substraction
print(a*b) # multiplication
print(a/b) # divison
print(a%b) # modulus

# Logical/Conditional Operators
# and, or, xor
print("*"*50)
print(a and b)
print(a or b)

# Bitwise Operator
# &,|,^
print("*"*50)
print(a & b)
print(a | b)

# Relational operators
# >,>=,==,=<,<
print("*"*50)
if(a > b):
    print(a)
else:
    print(b)

# Assignment Operators
# = (equal operator)
print("*"*50)
data = list(range(5))
print(data)

# Ternary Operators
# (Condition) ? OnTrue(Statement) : OnFalse(Statement)
print("*"*50)
res = a if a > b else b
print(res)
