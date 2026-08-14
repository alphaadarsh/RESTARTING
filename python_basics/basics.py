print('line 1 ')
print('line 2 ')
print('line 3 ')

# data types 
print('word') # string 
print(123) # integer
print(3.14) # float
print(True) # boolean

# operators
print(1 + 2) # addition
print(5 - 3) # subtraction
print(4 * 2) # multiplication
print(8 / 2) # division
print(10 // 3) # floor division
print(10 % 3) # modulus  ITS CALCULATES THE REMAINDER OF THE DIVISION
print(2 ** 3) # exponentiation or power operator

# we have many assisgnment operators in python. some commonly used assignment operators are:
x = 5 # assignment operator
x = x + 3 # addition assignment operator
x += 3 # addition assignment operator  
#  for -= same thing we can use for multiplication and division.

# to many operators in python we have to start  with  multiplication and division then addition and subtraction.

#  operators precedence is the order in which operators are evaluated in an expression. like in mathematics, python follows the order of operations (PEMDAS) to determine the precedence of operators. parentheses have the highest precedence, followed by exponentiation, multiplication and division, and finally addition and subtraction. when multiple operators of the same precedence appear in an expression, they are evaluated from left to right.

# variable  is just a bucket to store data in it.
name = "Alice"
age = 30       #this is integer 
height = 5.8   # this is float  

print(name)
print(age)
print(height)

# variabkle naming rules
# 1. variable names can only contain letters, numbers, and underscores. 
# they are case sensitive.
# 2. variable names should be descriptive and clear.

# input function is used to take input from the user.

input_name = input("Enter your name: ")
print("Hello, " + input_name + "!")

# what is data types in python?
# data types are the classification of data items.
# examples of data types in python are:
# 1. string
# 2. integer
# 3. float
# 4. boolean

# what is concatination?
# concatenation is the process of joining two or more strings together. 
#  commenly used operator for concatenation is + operator. 
# example: print("Hello, " + "World!") # output: Hello, World!

#  comment used for just for documentation purpose. it is not executed by the interpreter. we can use # symbol to write a comment in python. 

#  lets talk about comparison operators in python. comparison operators are used to compare two values and return a boolean result (True or False). some commonly used comparison operators are: 
print (5 > 3) # greater than
print (5 < 3) # less than
print (5 == 3) # equal to
print (5 != 3) # not equal to
print (5 >= 3) # greater than or equal to
print (5 <= 3) # less than or equal to 

#  lets talk about logical operators in python. logical operators are used to combine multiple conditions and return a boolean result (True or False). some commonly used logical operators are:
print (True and False) # logical AND
print (True or False) # logical OR
print (not True) # logical NOT   
#  if there is or and true in argument then it will return true. if there is and and false in argument then it will return false. if there is not then it will return opposite of the value.
# for and operator, if both conditions are true, the result is true; otherwise, it is false. for or operator, if at least one condition is true, the result is true; otherwise, it is false. for not operator, it negates the boolean value of the condition.
#  for not operator, it negates the boolean value of the condition. if the condition is true, not will return false; if the condition is false, not will return true. logical operators are often used in conditional statements and loops to control the flow of a program based on multiple conditions.

print("Hello, GitHub!")

x  = 5.32
y  = 10
z  = 6

# print(x + y) # addition
# print(x - y) # subtraction
# print(pow(x, z)) # exponentiation

result  = x + y
result  =  pow(x, z)
result = abs(x) # absolute value

print(x)


import math  

print(math.pi) # 3.141592653589793
print(math.sqrt(16)) # 4.0
print(f"{math.e:.2f}") # 2.718281828459045

result = math.ceil(3.2) # 4
result = math.floor(3.8) # 3

radius =  float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius
print(f"The circumference of the circle is: {circumference}")
