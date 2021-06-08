#python also supports functions like any other language
#you can pass data called parameters and return data

#to define a function we use the def keyword

def myFunction(txt):#this function has one paramater called txt
    print(txt)

#to invoke the function we simply call it like in any other language
txt = "Hello from a function"

myFunction(txt)

#we can also pass arguments to the function
#arguments are defined inside the function call
myFunction("Hello")#strings
myFunction(3)#integers
myFunction((1,2,3))#lists, tuples, sets, etc

#when passing arguments, we can only pass the amount specified in the function definition
def my_other_function(txt1, txt2):
    print(txt1 + " " + txt2)

my_other_function("Hello", "World")#this function accepts 2 args, no more, no less

#but we can get around to it.
#we can use arbitrary arguments (*args)

def special_function(*txt):#arguments will be passed as a tuple
    for x in txt:
        print(x)

special_function("Hello ","From ","a ","Special","Function")#we can now pass many arguments

#functions allow for keyword arguments 
def simple_function(txt1,txt2,txt3):
    print(txt3)

simple_function(txt1 = "hellow",txt2="hello?",txt3="Hello from keywords")

#this allows us to have a default params value 
def my_name(name = "John Doe"):#John Doe will be our default in this case
    print(name)

my_name()#proc the default param
my_name("Santiago")#we pass an arg

#if we don't know how many keyword arguments we are passing
# we can use arbitrary keyword arguments **kwargs

def a_person(**person):#the function will receive a dictionary
    print(person.items())

a_person(first = "Santi", last = "M", age="23",favColors=("red","black","blue"))

#function also have return statements

def one_more():
    return "Hello", "from return" #but unlike other languages, we ca return multiple things

word1, word2 = one_more()

print(word1+" "+word2)