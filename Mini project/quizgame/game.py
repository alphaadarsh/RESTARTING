# python quiz game
questions = ("What is the capital of France?",
              "What is the largest planet in our solar system?", 
              "What is the chemical symbol for gold?",
              "Who painted the Mona Lisa?", 
              "What is the longest river in the world?")

options = (("A. London", "B. Berlin", "C. Paris", "D. Madrid"),
           ("A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"),
           ("A. Go", "B. Au", "C. Ag", "D. Fe"),
           ("A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Michelangelo"),
           ("A. Amazon River", "B. Nile River", "C. Yangtze River", "D. Mississippi River"))

answers = ("C", "C", "B", "C", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, or D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("WRONG!")
        print(f"{answers[question_num]} is the correct answer.")
    question_num += 1



# Display the results
print("-------------------------")
print("RESULTS")
print("-------------------------")

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score =int( score / len(questions) * 100)
print(f"Your score is: {score}%")
# correct_answers = 0
# for i in range(len(questions)):
#     if guesses[i] == answers[i]:
#         correct_answers += 1

# print(f"You scored {correct_answers} out of {len(questions)} questions correctly.")