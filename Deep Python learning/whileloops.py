# while loops are used to execute a block of code repeatedly as long as a certain condition is true. The syntax for a while loop in Python is as follows:
#  in while loop if statement get true it will execute the block of code and if statement get false it will not execute the block of code.
#  in more simple code will run until get false statement.
#  we are using not here to check if the user input is not equal to "q" and if it is not equal to "q" then it will execute the block of code and if it is equal to "q" then it will not execute the block of code.
# i leanerd a lot

food = input("What is your favorite food?(q to quit) ") 
while not food == "q":
    print("You entered 'quit'. Exiting the loop.")
    # break  # This will exit the loop if the user enters 'quit'.
    food = input("What is your favorite food?(q to quit) ")  # This will prompt the user to enter their favorite food again.
print("bye!")  # This will print the user's favorite food after they exit the loop.


num = int(input("Enter a number: "))
while num < 1 or num > 10 :
    print(f"its not valid number {num} is not between 1 and 10. Please try again.")
    num = int(input("Enter a number: "))
print(f"Thank you! {num} is a valid number between 1 and 10.")  # This will print the user's favorite food after they exit the loop.