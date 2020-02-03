# print("hello World !")
# for i in range(22):
#     print("Unthinkable.co")

# Functions Demo
def myFunction(myVar):
    return myVar*myVar



value = myFunction(2)
print(value)

# for i in tple:
#     print(i)

# Different Types of Arguments in Functions
print("*"*50)
# Default Arguments

def counties(country = "India"):
    print("My Country is : ",country)


counties()
counties("USA")
counties("Europe")

# Arbitrary Arguments

def kids(*names):
    for i in names:
        print("The Kid name is : ",i,end=" -")

# Keword Argumetns
def cars(Honda,MarutiSuzuki,Hundai):
    print("The model car from Honda is : ",Honda)
    print("The model car from MarutiSuzuki is :",MarutiSuzuki)
    print("The model car from Hundai is : ",Hundai)

cars(Honda="Amaze",Hundai="Accent",MarutiSuzuki="Baleno")

# Arbitrary Keword Arguments

def premiumCars(BMW,Mercedes,Lamborgini,Audi,Rolls):
    print("The Premium Car is : ",BMW)
    print("The Premium Car is : ",Mercedes)
    print("The Premium Car is : ",Lamborgini)
    print("The Premium Car is : ",Audi)
    print("The Premium Car is : ",Rolls)

premiumCars(BMW="Model S",Mercedes="E edition",Lamborgini="Avantador",Audi="Q3",Rolls="S Class")


