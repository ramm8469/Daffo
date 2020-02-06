class Simple:
    # defining the properties 
    x = 21

    # defining the constructor : default constructor
    #def __init__(self):

    # defining the custom constructor
    def __init__(self,name,age):
        self.name = name
        self.age =  age

    # defining extra methods : Getters and Setters

    def getData(self):
        print(self.name)
        print(self.age)
    

    def setData(self,name,age):
        self.name = name
        self.age = age


#============== Creating Objects ==========================
    
myObj = Simple("john",23)

myObj.getData()

# __new__ : Keyword
# class demo:
#     def __new__(self):
#         return "Hello"

# d = demo()
# print(type(d))


# class demo1:
#     def __init__(self):
#         print("Hello ")
    
# dd = demo1()
# print(type(dd))
