#lets recall some function concepts
#first lets import math module

import math as mt

#lets create a function

#this function has a default parameter of 10 if nothing is passed
def square_root(my_number = 10):
    """this function takes an integer and returns its square root"""
    my_number = mt.sqrt(my_number)
    return my_number

#we pass no arguments so the default parameter is passed
print(round(square_root(),2))

#REMEMBER!!! Params are the var listed inside the parenthesis during func def
#arguments are the values passed when the 

#An important method in python is the dir()
#while not used in actual used during implementation, dir can provide 
#valuable information on methods

#lets see the methods inside the math module
print("\nThe following are the methods for this module:\n",dir(mt))

print("\n\nBuilt in python objects:\n",dir(__builtins__))

#when printed, we see some methods like __docs__ and __file__ etc as well
# as the standard math methods
#methods in __between__ are used to ger useful info.

print("\n", mt.__doc__)#this is the documentation method 
print("\n",square_root().__doc__)#the documentation of the function made above

#we will learn more about __special methods__ next module

