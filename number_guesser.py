import random

random_number = random.randint(0, 10)

guesses = 0
while True:
    guesses += 1
    guess = input("Guess a number: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("You have to type a number")
        continue

    if guess == random_number:
        print("You got it!")
        break
    elif guess > random_number:
        print("Your number is higher!")
    else:
        print("Your number is lower!")

print("You got it in", guesses, "guesses")



