#Guess a number game

import random
num=random.randint(1,100)
attempts=0
while True:
    guess = int(input("Enter a number : "))
    attempts += 1
    if guess<num:
        print("The number is low! Try another number ")
    elif guess>num:
        print("The number is high! Try another number ")
    else:
        print("Congratulations! You guessed the number correctly.")
        print(f"You guessed the number in {attempts} attempts.")
        print(f"The number was {num}.")
        print("Game Over!")
        break
    


