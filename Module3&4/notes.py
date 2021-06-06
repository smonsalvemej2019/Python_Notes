#strings are not complicated in python

txt = " \nHello World! It is a beautiful day! "

my_strng = "This is a string"

my_other_strng = 'This is also a string'

one_more_time = """ this string
can be 
in different lines """ #also ''' '''

#strings are arrays as well 
print(my_strng[0]) #T

for letter in my_other_strng:
    #prints the full string
    print(letter)

#we can get the length and check if there is words in a string

if "string" in my_strng: #checks if the word string is in string
    print(len(my_strng)) #then print the length 

#Slicing is a big part of strings in Python

print(txt[2:5])#prints from the second position to the fifth position
print(txt[:5])#prints from the begining to the fifth position
print(txt[5:])#prints from the fifth position to the end
print(txt[-5:-2])#prints from the negative fifth pos to the second to last position

#we can modify strings
print(txt.lower())#all lowercase
print(txt.upper())#all uppercase
print(txt.strip())#gets rid of any white space at the begining and the end (" hello " => "hello")
print(txt.replace("a","t"))#replaces all a's with t's 
print(txt.split(" "))#splits the string into substrings when it finds the separator (" ")

#we can concentrate strings with +
print(txt + my_strng)

#the format method allows us to pass variables to strings
age = "23"
name = "Santiago"
txt = "Hello my name is {} and my age is {}"
#if we put numbers inside {} we can enforce the order when we pass them

print(txt.format(age,name))# we pass the var to the text

