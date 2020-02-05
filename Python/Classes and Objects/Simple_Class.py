class  Simple:
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
    
# myObj = Simple_Class("john",23)

# myObj.getData()