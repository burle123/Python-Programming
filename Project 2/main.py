import random
n = random.randint(1,100)
guesses = 0
a = 0
while(a!=n):
    a = int (input ("Guess the number: "))
    guesses += 1
    if(a<n):
        print("Your guess is too low")
    elif(a>n):
        print("Your guess is too high")
  
print(f"Congratulations! You guessed the number {n} in {guesses} attempts.")  