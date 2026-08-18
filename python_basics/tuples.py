#  tUple ------------  immutable data type in python

marks =  (90, 80, 70, 60, 50 , 95 ,95 ,95 )  # this will create a tuple marks with the elements 90, 80, 70, 60, and we can also not use paranthesis to create a tuple but it is recommended to use parentheses for clarity and readability.
print (marks ,type(marks) , marks[2] , marks.index(70) )  # this will print the tuple marks and its type. 

print(dir(marks))  # this will print the list of all the methods available for the tuple object.  are faster than list because they are immutable and can be used as keys in dictionaries.  and also we can use index to get the value of the tuple.
print(help(marks))  # this will print the help documentation for the tuple object.