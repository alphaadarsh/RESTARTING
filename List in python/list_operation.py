# list operation  slicing concat repeat append start 
l1 = [3 , 4 , 5 , 6 , 7 , 8 , 9]
print(f"l1: {l1}")  # Output: l1: [3, 4, 5, 6, 7, 8, 9]
# slicing or also we can write like this l1[0:3]  # here 0 is starting index and 3 is ending indexp 
print(l1[1:6:1])

# concat 

l2 = [10, 11, 12]

l3 = l1 + l2

print(f"l3: {l3}")  # Output: l3: [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# repetation  
l4 = l1 * 2
print(f"l4: {l4}")  # Output: l4: [3, 4, 5, 6, 7, 8, 9, 3, 4, 5, 6, 7, 8, 9]
print (l1 * 2)

#  function append  add item in end of list  like fruits.append('orange')  # here we are adding orange in end of list  for adding in fronmt use insert function  like fruits.insert(0,'orange')  # here we are adding orange in front of list
fruits = ['apple', 'banana', 'cherry']
print(fruits.append('orange'))  # Output: None
print(f"fruits: {fruits}")  # Output: fruits: ['apple', 'banana', 'cherry', 'orange']
fruits.append('KIwi')
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange', 'KIwi']

#  extend  add item in end of list  like fruits.extend(['orange','kiwi'])  # here we are adding orange and kiwi in end of list  for adding in front use insert function  like fruits.insert(0,'orange')  # here we are adding orange in front of list
fruits.extend(['orange', 'kiwi'])
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange', 'KIwi', 'orange', 'kiwi']

# remove funtion remove item from list  like fruits.remove('orange')  # here we are removing orange from list  for removing in front use pop function  like fruits.pop(0)  # here we are removing first item from list
fruits.remove('orange')
print(fruits)  # Output: ['apple', 'banana', 'cherry', '

#  pop function remove item from list  like fruits.pop(0)  # here we are removing first item from list  for removing in front use remove function  like fruits.remove('orange')  # here we are removing orange from list
fruits.pop(0)   

print(fruits)  # Output: ['banana', 'cherry', 'KIwi', 'kiwi']

# reverse  sort  count membership  index  clear  copy  insert  extend  remove  pop  del  len  max  min  sum  any  all  sorted  reversed  

# REVERSE 
# SORT
# count
#  membership 
