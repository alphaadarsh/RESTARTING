#  typecasting is the process of converting one data type to another data type.

name  = "Alice"
age = 30
gpa = 3.5
is_student = True

print(type(name), type(age), type(gpa), type(is_student))  # output: <class 'str'> <class 'int'> <class 'float'> <class 'bool'>

gpa =  int(gpa)  # converting float to int
print(type(gpa))  # output: <class 'int'>
print(gpa)  # output: 3

age = float(age)  # converting int to float
print(type(age))  # output: <class 'float'>
print(age)  # output: 30.0

age = str(age)  # converting float to string 
print(type(age))  # output: <class 'str'>
print(age)  # output: 30.0
