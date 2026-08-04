#  dictionary => key value pair data type in python     collection of data which is unordered and unindexed. it does not allow duplicate members. it is mutable data type in python. we can add or remove elements from a dictionary. we can also perform mathematical operations on dictionaries like union, intersection, difference, symmetric difference etc.
marks = { 'math': 90, 'science': 80, 'english': 70, 'history': 60, 'geography': 50 , 'math': 95 , 'math': 95 }  # this will create a dictionary marks with the keys math, science, english, history, and geography and their corresponding values 90, 80, 70, 60, and 50. we can also not use paranthesis to create a dictionary but it is recommended to use parentheses for clarity and readability.

#  key  => value  

for key  in marks : 
    print (key , marks[key])  # this will print the key and its corresponding value in each iteration of the loop.