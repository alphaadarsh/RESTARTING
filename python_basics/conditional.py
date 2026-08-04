#  conditional statement 

age = int(input("Enter your age: "))
if age >= 18:    # we are using here indentation to define the block of code that will be executed if the condition is true. indentation is important in python as it defines the scope of the code block.
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")  # this is old method  to use else and than if but there is new method to use elif which is more efficient and readable. 

    