import random

computer = random.randint(1,3)

choice = input("1 - rock, 2 - paper, 3 - scissors: ")

if choice.isdigit():
    choice = int(choice)
    if choice == computer:
        print("Draw")
    elif choice == 1 and computer == 2:
        print("Computer won")
    elif choice == 1 and computer == 3:
        print("You won")
    elif choice == 2 and computer == 1:
        print("You won")
    elif choice == 2 and computer == 3:
        print("Computer won")
    elif choice == 3 and computer == 1:
        print("Computer won")
    elif choice == 3 and computer == 2:
        print("You won")
    else:
        print("Please enter number 1-3")
else:
    print("You have to type a number!")

print(choice, computer)