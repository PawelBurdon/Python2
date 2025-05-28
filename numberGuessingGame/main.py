import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(user_guess, actual_answer, attempts):
    if user_guess == actual_answer:
        print("You won!")
    elif user_guess > actual_answer:
        print("Too high!")
        return attempts - 1
    else:
        print("Too low!")
        return attempts - 1
    
def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == "hard":
        return HARD_LEVEL_TURNS
    elif difficulty == "easy":
       return EASY_LEVEL_TURNS
    

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
number = random.randint(0, 100)

attempts = set_difficulty()

while True:
    print(f"You have {attempts} remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    attempts = check_answer(user_guess, number, attempts)
    if user_guess == number or attempts == 0:
        break
    