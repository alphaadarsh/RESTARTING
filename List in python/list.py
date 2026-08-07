# literals  is lik data which is used to represent fixed values in python. There are different types of literals in python like string literals, numeric literals, boolean literals, etc. 


# list is data structure in python which is used to store multiple items in a single variable. It is one of the most commonly used data structures in python. Lists are ordered, changeable, and allow duplicate values. They are defined by enclosing elements in square brackets [].

#  can we store different data types in a list?  yes we can store different data types in a list.
# #  in single list we can store different data types like int, float, string, boolean, list, tuple, set, dictionary etc.
# name = "John"
# age = 25
# percentage = 85.5

student = ["John", 25,  85.5]  # list containing different data types   
print(type(student))  # Output: <class 'list'>
print(student)  # Output: ['John', 25, 85.5]

day_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]  # list containing string literals  
# indexing like  [0, 1, 2, 3, 4, 5, 6]  # index of list starts from 0 and ends at n-1 where n is the number of elements in the list

print( f"last day of week is: {day_of_week[6]}")  # Output: last day of week is: Sunday

# length of list   
print( f"Length of  list is: {len(day_of_week)}")  # Output: Length of student list is: 7