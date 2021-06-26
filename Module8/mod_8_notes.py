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

#is python parameters passed by reference or by value?
#Neither, python uses a mechanism called pass-by-object.
#we can simply think of pass-by-object as giving things(a function a datatype) a name (var name)
#in python we bind a name to an object!!!!
#immutable objects like strings can be thought of as pass by value and mutable objects like lists are mustable

#an example 
#lets define a immutable variable
my_string = "\nThis is my string outside the function\n"

#and define a function that will change the immutable
def mutate_strng(my_string):
    my_string = "\nIs something different now inside the function\n"
    print(my_string)

#passing the string to the function will change the value ONLY INSIDE the function scope and not in the global
mutate_strng(my_string)
print(my_string)

#lets define mutable variable
my_list=['Hello','this is my','mutbale','variable']

#and define a function that will change our mutable
def mutate_list(my_list):
    my_list[2],my_list[1] = 'mutated', 'this is now my'

#notice that the variable changed in the global scope
print(f"\n{my_list}")
mutate_list(my_list)
print(f"\n{my_list}")

#scopes are are also very important yet very simple in python, we have four types:
#LOCAL: Var x is inside the innermost function g()
#ENCLOSING: if there is two nested functions f() and g() and if var x is not in the local scope of inner function g()
#then the interpreter looks for x in the enclosing function f()
#GLOBAL: If x is not inside any function f() or g() then it must me somwhere in the global scope (defined in the main program)
#BUILT-IN: If x is not in the global scope then it must be a python built-in object.




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


