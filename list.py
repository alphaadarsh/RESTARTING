# list is colection of data which is ordered and changeable. it allows duplicate members.
marks = [90, 80, 70, 60, 50]

print (marks ,type(marks))
    #  length of list
print (len(marks))  # this will print the length of the list marks.

# index 
print (marks[0])  # this will print the first element of the list marks.
print (marks[-1])  # this will print the last element of the list marks.    
 
#  slicing   list [ start : end : step]  # this will print elements from index start to end-1 with step size of step.
print (marks[1:4])  # this will print elements from index 1 to 3.
for score in marks :
    print (score)  # this will print each element of the list marks.

marks.append(40)  # this will add the element 40 to the end of the list marks.
print (marks)  # this will print the updated list marks.

marks.insert(2, 75)  # this will insert the element 75 at index 2 of the list marks.
print (marks)  # this will print the updated list marks.