# Here in this file, we are going to see the concept of 
# Context Manager in Python.

# Using Classes
# Creating a custom context manager
class file_opener:

    # Definig Constructor
    def __init__(self,file_name,mode):
        self.file_name = file_name
        self.mode = mode
    
    # Defining the enter method
    def __enter__(self):
        self.file_obj = open(self.file_name,self.mode)

        # return the file object
        return self.file_obj
    
    # Defining the exit method
    def __exit__(self,exc_type, exc_value, exc_traceback):
        # Close the file, when getting out of the context manager
        self.file_obj.close()



# Now creating the object of the custom context managers
with file_opener("Test.txt",'w') as writer:
    writer.write("This is a testing\n")
    writer.write("Using the context manager")

# check whether file is closed or not...
print(writer.closed)

# =====================================================
print("*"*50)
# Using Function with a decorator
# for using with a function, we need to import contextlib module
# and import contexmanager decorator

from contextlib import contextmanager

@contextmanager
def file_opener_func(fname,mode):
    try:
        # enter method's code
        file_object = open(fname,mode)
        yield file_object
    except:
        print("some error occured")
# tear down code...
    # exit method's code
    finally:
        file_object.close()
    


# now, calling that function
with file_opener_func("abc.txt",'w') as func_writer:
    func_writer.write("This is from file opener funciton\n")
    func_writer.write("using the Context manager decorator")

# check whether file is closed or not...
print(func_writer.closed)

