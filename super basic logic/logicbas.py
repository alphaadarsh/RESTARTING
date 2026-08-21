num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))
result = num_1 + num_2 

# print(f"sum of num 1 and num 2 is {result:.2f}") 

operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    result = num_1 + num_2
    print(f"The sum of {num_1} and {num_2} is: {result:.2f}")
elif operation == "-":
    result = num_1 - num_2
    print(f"The difference of {num_1} and {num_2} is: {result:.2f}")
elif operation == "*":
    result = num_1 * num_2
    print(f"The product of {num_1} and {num_2} is: {result:.2f}")
elif operation == "/":
   if num_2  != 0 :
       result = num_1 / num_2
       print(f"The quotient of {num_1} and {num_2} is: {result:.2f}")
   else:
       print("Error: Division by zero is not allowed.")
elif operation == "**":
    result = num_1 ** num_2
    print(f"The result of {num_1} raised to the power of {num_2} is: {result:.2f}")
elif operation == "%":
    result = num_1 % num_2
    print(f"The modulus of {num_1} and {num_2} is: {result:.2f}")
elif operation == "//":
    if num_2 != 0:
        result = num_1 // num_2
        print(f"The floor division of {num_1} by {num_2} is: {result:.2f}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter one of the following: +, -, *, /, **, %.")

