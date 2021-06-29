#lets go back to dictionaries and sets

#sets are unordered, unindexed, and unchangeable.

my_set = {"hello", 2 , "All!", 2}#sets are defined with brackets {}

print(my_set,"\n")#notice that the output will not be in the same order as the variable definition and there is a "2" missing

#we can no access the set trough regular indexing nor we can change the items within it once created
#however, we can use for loops to access the set and we can ADD (not delete) items

for i in my_set:
    print(i)

print("All!" in my_set)#will return true  

#we can use the add method
my_set.add("hello from add!")
print(f"\n{my_set}")

#or add items from another set using the update method
your_set = {"bitcoin", "Ether", "Doge"}
my_set.update(your_set)
print(f"{my_set}")

#we can discard the last item using the .pop()(remember that sets are unordered!)method or an specific item with the .discard() methods
my_set.discard("Doge")#.remove() will work too. Both will raise an error if the passed arg is not found
print(f"\n{my_set}")

#.clear() will empty the set
#del keyword will delete the whole set

#for more methods please go to w3schools


#Dictionaries is the most interesting built in data structure.
#Dictionaries resemble JavaScripts objects which itself resembles JSON. 
#Dictionaries are more prevalent in web design
#they are ordered (python 3.7+) changable and does not allow duplicates

#lets define our dictionary 

crypto = {
    "Bitcoin" : {
        "symbol": "BTC",
        "release": 2009,
        "price": 34737,
    },
    "Ethereum":{
        "symbol": "ETH",
        "release": 2015,
        "price": 2130
    },
    "Stellar Lumens":{
        "symbol": "XLM",
        "released": "unknown",
        "price":0.27
    }
}

print(f"\n\n{crypto}")

#we can access items with the .get(<key>) methods or we can use the index dictionary[<key>]

print(f"\n\n{crypto['Bitcoin']}")
print(f"\n{crypto.get('Stellar Lumens')}")

#this way we can access each individual item and possibly make modifications
#keys play a very important role. Usually when using JSON it is easier to find keys than to print the whole structure
#the .keys() method will return the keys

print(f"\n{crypto.keys()}")

#.values() will return all values

print(f"\n{crypto.values()}")

#lets add a new value
crypto["Doge"] = {"symbol":"D", "release":2013,"price":0.26}

print(f"\n{crypto.items()}")#will return each item

#we can check if a key exist with "in"

#for more on dictionary methods please visit w3schools