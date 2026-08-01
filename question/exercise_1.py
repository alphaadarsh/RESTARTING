# take 2 integers from user and print the sum of all even numbers between them
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# next print the fiorst number  btw 1 and 1000 that iws divisible by both number  
for i in range(1, 1001):
    if i % num1 == 0 and i % num2 == 0:
        print(i)