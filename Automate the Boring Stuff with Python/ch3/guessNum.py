import random
secretNum = random.randint(1, 20)
print("I think of number between 1 and 20")

for guessesTaken in range(1, 7):
    print("Take a guess.")
    guess = int(input())
    if guess < secretNum:
        print("Your guess is too low.")
    elif guess > secretNum:
        print("Your guess is too high.")
    elif guess == secretNum:
        print("Good job." + str(guessesTaken) + " guess " + str(guess))
        break;
    else:
        print("Nope The number I thinking of was " + str(secretNum))


