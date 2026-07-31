# lets talk about range  
from posixpath import sep
from tracemalloc import start, stop


num = range(10) # this will create a range object that represents the numbers from 0 to 9.
print(list(num)) # this will print the numbers in the range by converting the range object to a list.
# 1 to 5  
range (1 , 6 ) # this will create a range object that represents the numbers from 1 to 5.

range(start, stop, step = 1 ) # this will create a range object that represents the numbers from start to stop with a step of step. 
