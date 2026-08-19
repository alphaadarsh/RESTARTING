capitals = {"USA": "Washington, D.C.",  # a collection of key-value pairs.  and also we can use index to get the value of the dictionary. no duplicate keys are allowed in a dictionary.  and also we can use index to get the value of the dictionary.
            "France": "Paris", 
            "Japan": "Tokyo" , 
            "India": "New Delhi",
            "germany" : "berlin",
            "italy" : "rome",}
# print(dir(capitals))  # this will print the list of all the methods available for the dictionary object.  are mutable data type in python.  and also we can use index to get the value of the dictionary.

# print(help(capitals))  # this will print the help documentation for the dictionary object.  are mutable data type in python.  and also we can use index to get the value of the dictionary.

print(capitals.get("USA"))  # this will print the value of the key "USA" in the dictionary capitals.  and also we can use index to get the value of the dictionary.
print(capitals["France"])  # this will print the value of the key "France"

if capitals.get("Canada") :
    print("that capitals exists")
else: 
    print("that capitals does not exists")


capitals.update({"Canada": "Ottawa"})  # this will add the key "Canada" and its value "Ottawa" to the dictionary capitals.  and also we can use index to get the value of the dictionary.
print(capitals)  # this will print the dictionary capitals.  and also we can use index to get the value of the dictionary.

capitals.pop("USA")  # this will remove the key "USA" and its value from the dictionary capitals.  and also we can use index to get the value of the dictionary.
print(capitals)  # this will print the dictionary capitals.  and also we can use
capitals.popitem()  # this will remove the last key-value pair from the dictionary capitals.  and also we can use index to get the value of the dictionary.
print(capitals)  # this will print the dictionary capitals.  and also we can use index to get the value of the dictionary.

# to get all of 5the key 
key = capitals.keys()  # this will return a view object that displays a list of all the keys in the dictionary capitals.  and also we can use index to get the value of the dictionary.
print(key)  # this will print the view object that displays a list of all the keys
#  technically key is an object which resammble a list but it is not a list.  and also we can use index to get the value of the dictionary.

# for iterate we can use for loop to iterate through the view object that displays a list of all the keys in the dictionary capitals.  and also we can use index to get the value of the dictionary.
for key in capitals.keys():  # this will iterate through the view object that displays a list of all the keys in the dictionary capitals.  and also we can use index to get the value of the dictionary.
    print(key)  # this will print each key in the dictionary capitals.  and also we can use index to get the value of the dictionary.

print()
value = capitals.values()  # this will return a view object that displays a list of all the values in the dictionary capitals.  and also we can use index to get the value of the dictionary.
print(value)  # this will print the view object that displays a list of all the values

for value in capitals.values():  # this will iterate through the view object that displays a list of all the values in the dictionary capitals.  and also we can use index to get the value of the dictionary.
    print(value)  # this will print each value in the dictionary capitals.  and also we can use index to get the value of the dictionary.

items = capitals.items()  # this will return a view object that displays a list of all the key-value pairs in the dictionary capitals.  and also we can use index to get the value of the dictionary.
print(items)  # this will print the view object that displays a list of all the key-value pairs in the dictionary capitals.  and also we can use index to get the value of the dictionary.