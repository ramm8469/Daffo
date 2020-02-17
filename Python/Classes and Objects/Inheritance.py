class employee(object):
    # Parent/Base Class
    # Defining the constructor
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = ""
    
    # method to create email
    def generateMail(self):
        self.email = self.first+"."+self.last+"@comapany.com"
        return self.email

    # Special Dunder/magic built-in methods in python for an objects
    
    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first,self.last,self.pay)

    def __str__(self):
        return "Employee('{}','{}','{}') from str".format(self.first,self.last,self.pay)



    


# now creating the objects of employee

john = employee("john","doe",15000)
jackie = employee("jackie","russel",20000)

# Generating email ids for the employees
print(john.generateMail())
print(jackie.generateMail())

print("*"*50)

# Now creating the child/subclasses of the employee classes
# Inheriting the employee class as base class

class Developer(employee):

    # defining the constructor
    def __init__(self,first,last,pay,program_lang):
        # calling the base class constructor
        # super().__init__(first,last,pay)
        employee.__init__(self,first,last,pay)# this is used in case of multiple inheritance
        # adding the extra property "Programming Language" to the Developer class
        self.program_lang = program_lang

    
    # Defining method for developer profile
    def dev_profile(self):
        print("The Developer have skills of "+self.program_lang+" Language")


# Now creating the objects of Developer class
ram = Developer("ram","mohan",15000,"Python")
shyam = Developer("shyam","mohan",30000,"Java")

# Generating the email ids of developers
print(ram.generateMail())
print(shyam.generateMail())

print("*"*50)

# Getting the profile of the developer
ram.dev_profile()
shyam.dev_profile()

print("="*50)

# ========================================================================
# Here in this file we are going to discuss the dunder method
# avaliable in python

# Note  : All these special methods should be defined in the class to whose
# objects/instances we want to pass in these mehtods...

# __init__ : This method is used as constructor
# __repr__ : it is meant for unambigous representation
#  of object and sholuld be used for debuging and loging purposes.

#  ex : repr(object_name) : returns the object representation




print(repr(john))
print(repr(jackie))


# __str__: this is also used for object representation, 
# but in more readable way to the end users.


print("+"*50)
print(str(john))
print(str(jackie))

# how these __repr__() and __str__() methods executes internally
print(jackie.__repr__())
print(jackie.__str__())

print("=="*40)


# how + operator internally work
print(1+2)
print(int.__add__(1,2))

print("a"+"b")
print(str.__add__("a","b"))
