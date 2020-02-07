# Here in this demo, we are going to see the difference between Class Variables
# and the Instance Variables

# Class variables are those variables, which are written straigth in class, 
# above of all the methods and constructor of the class

# Class variables are accessible to all the instances of the class and shared 
# common along all instance

# Instances variables are those variables,which are written in the constructor 
# of the class, by which each instance can have it's own variables and each
# Instances var have different values

# creating a class with class variable

class shark:
    # creating class variables
    animal_type = "Fish"
    location = "Ocean"


# now create the object of the class shark and can access the class variable with
# dot (.) operator
print("*"*50)
print(shark.animal_type)
print(shark.location)



# Now creating a class with Instance Variables

class shark1:

    # defining the constructor
    def __init__(self,name,age):
        self.name = name
        self.age = age
    

# creating the object of the class shark1

jame = shark1("jame",21)
print("*"*50)
print(jame.name)
print(jame.age)

# creating another object of the class shark1

jone = shark1("jone",23)
print("*"*50)
print(jone.name)
print(jone.age)


# now, creating a class where we use both the class variable and the instance
# variable :  this may occur while developing a project, where we may require
# to have both class variable and instance variables...

class whale:
    # Class Variables
    animal_type = "Fish"
    location = "Ocean"

    # constructor
    def __init__(self,name,age):
        self.name = name
        self.age = age

    

# create the object of the whale class
john = whale("john",25)
print("*"*50)
print(john.name)
print(john.age)
print(john.animal_type)
print(john.location)


