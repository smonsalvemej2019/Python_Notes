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


#python also has if-else statements and loops

x = 9
y = 15
z = 200

#reminder: python cares for indentation
if x > y:
    print(f"{x} is greater than {y}")
elif x == y:#elif is the else if statement of python
    print(f"{x} is equal to {y}")
else:
    print(f"Hello from else")

#we can also do one line statements

if x < y : print(f"hello from a one line if else statement")

#we can also do a ternary operator approach

print("Z is greater") if z > x and z > y else print("y is greater") if y > x else print("x is greater")

#we have the keywords "and", "or" to represent && and || 

#we can also use the "pass" if we have an empty if-else statement. pass is considered a null operation
#anf it is useful when writing stubs

#python also offers looping 
#the while loop is pretty standard
print('loops \n')
while x < y:
    print(x)
    x += 1
#but it is also closley related with the if-else statements
x = 9
while y < x: #because this is not true 
    print(x)
    x += 1
else:
    print(f"\n{y} is not less than {x}\n")#this code will run

#we can also use the "continue" key word to skip an iteration and "break" to stop the loop
x = 1
while x < 20:
    x += 1
    if x == 11:
        print("Hello from the continue statement")
        continue
    elif x == 15:
        print("\nHello from break statement\n")
        break
    print(x)

#for loops are a bit more interesting
#we can loop thought strings

print("\nfor loops\n")

long_word = "antidisestablishmentarianism"

for letter in long_word: #similar to JS loops
    print(letter)

print("\n")
# we can also use the break statement 

for letter in long_word: 
    if letter == 'd':
        break
    print(letter)

print("\n")
#and the continue statement
for letter in long_word: #will skip all a
    if letter == 'a':
        continue
    print(letter)

print("\n")
#if we want to make a loop that iterates trough a specific range, we can 
#use the range() function

for x in range(10):#the range is from 0 to 9 
    print(x)

for x in range(10,20):#the range is from 10 to 19 
    print(x)

for x in range(20,100,10):#the range is from 20 to 100 with an increment of 10 
    print(x)
else:
    print("end of loop")
    #else will execute when the for loop ends but not when
    #the loop is interrupted by a break

