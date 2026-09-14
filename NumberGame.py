import random

random_number = random.randint(1, 50)

print(" Number Guessing Game")
print("Guess the  number between 1 and 50.")
print("You have 5 attempts ")

for attempt in range(1, 6):

    attempts = int(input("Enter your guess: "))

    if attempts == random_number:
        print("Correct! You guessed the number!")
        print("You got it in", attempt, "attempt(s).")
        break

    else:
        difference = abs(random_number - attempts)

        if difference <= 3:
            print("Hot!!!")
        elif difference <= 7:
            print("Warm!")
        elif difference <= 15:
            print("Cold!")
        else:
            print("Ice Cold!")

        print("Wrong guess!")

        print("Attempts left:", 5 - attempt)

else:
    print("Game Over!")
    print("The random number was:", random_number)





