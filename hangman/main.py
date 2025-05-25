import random as rand

word_list = ["flowers", "onion", "ring"]


chosen_word = word_list[rand.randint(0, len(word_list)-1)]
# print(chosen_word)


placeholder = ""
for word in chosen_word:
    placeholder += "_"
print(placeholder)

lives = 6

correct_letters = []


while(True):
    print("Lives left:", lives)
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += guess
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print("You lose!")
            break

    if "_" not in display:
        print("You win!")
        break