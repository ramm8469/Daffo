# Positional Arguments Function
def func_positional(*args):
    print(args)
    print(type(args))

# Keyword Arguments Function
def func_keyword(**kargs):
    print(kargs)
    print(type(kargs))


# calling both function

func_positional(1,2,"name",False,33.33)
print("*"*50)
func_keyword(name = "Ram",integer = 2,float_val  = 33.33,boolean = False)