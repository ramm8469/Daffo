# # print("hello World !")
# # for i in range(22):
# #     print("Unthinkable.co")

# # Functions Demo
# def myFunction(myVar):
#     return myVar*myVar



# value = myFunction(2)
# print(value)

# # for i in tple:
# #     print(i)

# # Different Types of Arguments in Functions
# print("*"*50)
# # Default Arguments

# def counties(country = "India"):
#     print("My Country is : ",country)


# counties()
# counties("USA")
# counties("Europe")

# # Arbitrary Arguments

# def kids(*names):
#     for i in names:
#         print("The Kid name is : ",i,end=" -")

# # Keword Argumetns
# def cars(Honda,MarutiSuzuki,Hundai):
#     print("The model car from Honda is : ",Honda)
#     print("The model car from MarutiSuzuki is :",MarutiSuzuki)
#     print("The model car from Hundai is : ",Hundai)

# cars(Honda="Amaze",Hundai="Accent",MarutiSuzuki="Baleno")

# # Arbitrary Keword Arguments

# def premiumCars(BMW,Mercedes,Lamborgini,Audi,Rolls):
#     print("The Premium Car is : ",BMW)
#     print("The Premium Car is : ",Mercedes)
#     print("The Premium Car is : ",Lamborgini)
#     print("The Premium Car is : ",Audi)
#     print("The Premium Car is : ",Rolls)

# premiumCars(BMW="Model S",Mercedes="E edition",Lamborgini="Avantador",Audi="Q3",Rolls="S Class")


class cat:
    hand = 4
    def __init__(self):
        self.eye = 2
        self.legs = 4
    
    def run(self):
        print("Cat runs with its ",self.legs)
    
    def runs(self,*args,**kargs):
        print("cat runssssss")



kitty = cat()

kitty.run()
# kitty.runs()

cat.run(kitty)
print(kitty.eye)
print(kitty.legs)
# print(kitty.color)
kitty.color = "red_white"
print(kitty.color)

kitty_1 = cat()

kitty_1.run()
print(kitty_1.eye)
print(kitty_1.legs)
# print(kitty_1.color)
kitty_1.eye_color = "Blue"
print(kitty_1.eye_color)
# print(kitty.eye_color)

print(cat.hand)
print(kitty.hand)
print(kitty_1.hand)

cat.hand = 5

print(cat.hand)
print(kitty.hand)
print(kitty_1.hand)
kitty.hand = 6

print(cat.hand)
print(kitty.hand)
print(kitty_1.hand)
