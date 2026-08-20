
import random   

lowes_num = 1 
high_num = 100 

answer = random.randint(lowes_num, high_num)

print(answer)

guesses = 0 
is_running = True 

print("Python number guessing game ")
print (f"select a number between{lowes_num} and {high_num}")

while is_running:
    guess = input("enter your guess:")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < lowes_num or guess > high_num:
            print(f"please select a number between {lowes_num} and {high_num}")
        elif guess < answer:
            print("too low")
        elif guess > answer:
            print("too high")
        else:
            print(f"Correct! The answer was {answer} and you got it in {guesses} guesses")
            print(f"number of guesses: {guesses}")
            is_running = False
    else :
        print("invalid guess")
        print (f"please print the number between {lowes_num} and {high_num} next time")

          
