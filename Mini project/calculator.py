# mini project 1:  create a simple calculator that can perform basic arithmetic operations like addition, subtraction, multiplication, and division. The calculator should take two numbers and an operator as input from the user and display the result of the operation.

#  take input from the user 
num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: ")) 
operator = input("Enter the operator (+, -, *, / , ** ,  % ): ")

if operator == "+": 
    result = num_1 + num_2
    print("The result of addition is: " , result)
elif operator == "-":
    result = num_1 - num_2
    print("The result of subtraction is: " , result)
elif operator == "*":
    result = num_1 * num_2
    print("The result of multiplication is: " , result)
elif operator == "/":
    result = num_1 / num_2
    print("The result of division is: " , result)
elif operator == "**":
    result = num_1 ** num_2
    print("The result of exponentiation is: " , result)
elif operator == "%": 
    result = num_1 % num_2
    print("The result of modulus is: " , result)

else:
    print("Invalid operator")