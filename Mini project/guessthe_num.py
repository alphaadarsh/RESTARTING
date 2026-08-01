import random 

def play_game():
   lucky_num = random.randint(1, 50)  # Generate a random lucky number between 1 and 50\

   while True: 
       guess = int(input("Guess the lucky number between 1 and 50: "))  # Prompt the user to guess the lucky number

       if guess ==  lucky_num:
           print("Congratulations! You guessed the lucky number:", lucky_num) 
           break  # Exit the loop if the user guesses correctly
       
       elif guess < lucky_num:
           print("Too low! Try again.") 

       else:
            print("Too high! Try again.")

            print("Thanks for playing the game!")

play_game()  # Call the function to start the game
