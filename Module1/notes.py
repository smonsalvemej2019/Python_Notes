#import modules
import math #import keyword used to import libraries

#Syntaxes

#None...Python has not syntax. Well it does, but remember that you do not have to 
#define your data type

#Basic datatypes

num = 1 #this is an integer
fnumber = 2.8 #this is a decimal
letter = 'a' #this is a character 
strng = "Hello Painful world" #this is a string

#I/O. 
#like any other language there is basic i/o 

myInput = input("Enter a number of your choice: ")
int(myInput) ##when we get input it is in a string format, int will change it to an integer
print('This is my output:', myInput)

#we can also import libraries like any other language 
#python comes with a lot of libraries out of the box
#libraries out of the box
#(check the the import section at the top)
#the math library is a useful standard library

#example program: Circumference program 

rad_in = input("Enter the input of your circle: ")
rad_in = float(rad_in)

circum = 2 * math.pi * rad_in
area = math.pi * (rad_in ** 2)#the ** represents power

#putting f in front of print, we can pass the var to the string, similar to backticks in JS
#IMPORTANT: THIS CAN ONLY BE USED IN PYTHON 3
print(f"The area of your circle is: {area} and circumference is: {circum}")

#the math library has many many useful methods

#there is other reserved words that could be useful foe debugging
myStrng = "The type reserved word will tell you the type of var we are dealing with"
print(type(myStrng)) # a string of course

#python also lets us represent numbers in different bases

anOctal = 0o12 #base 8

aHex = 0x12 #base 16

aBin = 0b101 #base 

#python also its own built-in datatypes
#each datatype is characterized by the type of brackets used

#list items are ordered, changebale, indexed and allows duplicates
#because they are indexed it allows the the [n]
#because it is ordered, new items will be added to the end of the list
#for list methods please look at w3 schools 

my_list = ['banana', 'apple', 1] #[] for lists
print(f"this is my list: {my_list}")


#tuples are ordered and unchangeable 
my_tuple = ('banana',3,'kava') #() for tuple
print(f"this is my tuple: {my_tuple}")

#sets are unordered and not indexed 
my_set = {'this','is','my set', 9000} #{} for sets
print(f"this is my set: {my_set}")

#dictionaries are ordered(python 3.7 on) changebale and do now allow duplicates

my_dict = {
    "name": "santi",
    "age": 23,
    "favColor": "blue",
    "student": True #booleans are capitalize in python
}
print(f"this is my dictionary: {my_dict}")

#we use \ to indicate the code is extended to the line after
print(f"We can also acccess the tuples individually:\n \
hello my name is {my_dict['name']} and im {my_dict['age']} years old")
#we use '' inside "" 
#dictionaries are very similar to JS objects and can be nested. 
#for more info please check w3 schools.

