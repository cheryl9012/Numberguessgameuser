# Guess the number game Python project (User)
import random
print("Guess the number between 1 and 100!")
# generate a random number
number = random.randint(1, 100)

while True:
    guess = int(input("Enter your guess number: "))
    if guess < number:
        print("Too low number, try again.")

    elif guess > number:
        print("Too high number, try again.")

    else:
        print("Congratulations, you guessed the right number!")
        break
    
   