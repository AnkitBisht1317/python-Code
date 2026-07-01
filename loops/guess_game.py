import random
jakpot = random.randint(1,100)

guess = int(input("Guess a number between 1 to 100 :"))
counter = 1
while guess != jakpot:
    if guess < jakpot:
        print("Your guess is too low.")
    else: 
        print("Your guess is too high.")
    guess = int(input("Guess again: "))
    counter += 1

print(f"Congratulations! You've guessed the number {jakpot} in {counter} attempts.")    
