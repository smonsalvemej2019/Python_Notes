#In module 1 we went over arrays
#In module 7 we dive deep into lists and tuples 

#recall 
#A list is defines with brackets []

my_list = ["Hello","from","a list", 1, 2, 3, 4, True, False]
print("This is a", type(my_list))
print(my_list)

#A tuple is defined with parenthesis ()
my_tuple = ("Hello","from","a tuple", 1, 2, 3, 4, True, False)
print("This is a", type(my_tuple))
print(my_tuple)

#IMPORTANT
#LISTS are ordered, mutable and allows duplicates 
#LISTS are ordered, immutable and allows duplicates

#because they are both ordered we can use indexes to access them [n]

#we can also create these var with their constructors

my_tuple = tuple(("hello tuple","from","constructor"))
my_list = list(("hello list","from","constructor"))


