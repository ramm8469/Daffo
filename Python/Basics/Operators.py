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

# Membership Operator
# in,not in
print("*"*50)

mobiles = ['Samsung','Apple','RealMe','Mi','AT&T']

# in operator
if 'RealMe' in mobiles:
    print("That's the new Phone")
else:
    print("All are old Models")

print("*"*50)
# not in operator
if 'MicroMax' not in mobiles:
    print("No Indian Brand Mobiles")
else:
    print("Micromax Mobiles are available")


#==========================================
# Identity Operators
# Like is,not is
# These operator are used to check the value of variables (two or more variables)
print("*"*50)
collection = ["name",1,3,44.44,False,"Ram"]

# Is Opertaor : It Checks whether both the value are of same of two differen varibles
for i in collection:
    for j in collection:
        print("I : ",i," == J : ",j)
        if i is j :
            print("Both are Same Data Type")
        else:
            print("Both are Different Data type")


# not is Operator : It Just the reverse of the is operator
print("*"*50)
for i in collection:
    for j in collection:
        print("I : ",i," !== J : ",j)
        if i is not j :
            print("true")
        else:
            print("false")