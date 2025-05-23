print("Welcome to qiuz!!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okey! Let's play!")

counter = 0
    
answer = input("What does WWW stand for? ")
if answer.lower() == "world wide web":
    print("Correct!")
    counter += 1
else:
    print("Incorrect!")

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    counter += 1
else:
    print("Incorrect!")

print("You got " + str(counter) + " questions correct!")