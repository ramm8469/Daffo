# In this file, we are going to see the Different types of Conditionals available
# in python
a = 10
b = 20
# if
print("*"*50)
if a is b:
    print(True)

# if - else
print("*"*50)
if a is b :
    print(True)
else:
    print(False)

# if-elif-else // nesting
print("*"*50)
if a > b :
    print(" A is greater than B")
elif b > a :
    print("B is greater than A")
else:
    print("A and B both are equal")

# switch case
print("*"*50)
fruits = ['Banana','Mango','Apple']

# for i in fruits:
#     switch(i):

# Unlike any other programming languages, 
# In python we don't have switch cases
# Instead of switch case, we use dictionary as a replacement

switch = {
    'Banana' : "A Healthy,tasty and Iron prosperous fruit",
    'Mango' : 'Sweet,Juicy,King of all fruit',
    'Apple' :'Sweet,tasty,EveryDay fruit'
}
for i in fruits:
    print(switch.get(i))
