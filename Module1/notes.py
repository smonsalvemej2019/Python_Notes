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
print(f"The area of your circle is: {area} and circumference is: {circum}")

#the math library has many many useful methods

#there is other reserved words that could be useful foe debugging
myStrng = "The type reserved word will tell you the type of var we are dealing with"
print(type(myStrng)) # a string of course

#python also lets us represent numbers in different bases

anOctal = 0o12 #base 8

aHex = 0x12 #base 16

aBin = 0b101 #base 2

