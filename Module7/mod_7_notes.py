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

my_tuple = tuple(("hello tuple","from","constructor")) #notice that they are both inside parentheses
my_list = list(("hello list","from","constructor"))


#we can have lists of lists, tuples of tuples etc

print("\n")

list_of_lists = [["my","first","list"],["my","second","list"]]

for lists in list_of_lists:#prints both lists
    print(lists)

print("\n")
for lists in list_of_lists:#prints each word in each list 
    for word in lists:
        print(word)
    print("\n")

#works with tuples too!

#we can think of lists and tuples as as spreadsheet!

list_of_lists = [["Name:","Age","Occupation"],["Santi","23","student"],
                ["Allen","27","marketing specialist"],["Matt","21","gamer"]]
for entry in list_of_lists:
    print(entry[:])#if we put the index [n] we can diplay columns slicing included!

#operators also work on lists
# (+) is concatenation
# (* int) is multiplication of a list by the val of the int
# (> and <) checks if each val is less than or greater than
# (in) checks for membership

#lists and tuples also have methods but please go to W3Schools for more on those