import random as r
import time as t

randNumber = r.randint(1, 100)
guesses = 0
userGuess = None

print("Welcome to the Number Guessing Game!")
print()
print("Guess the number between 1 and 100")
print()
t.sleep(2)
print()

while(userGuess != randNumber):

    print()
    userGuess = int(input("Enter your guess: "))
    print()
    guesses += 1
    if userGuess == randNumber:
        print("🎉 You guessed it right!")
        print()
    else:
        if(userGuess > randNumber):
            print("❌ You guessed it wrong! Enter a smaller number")
            print()
        else:
            print("❌ You guessed it wrong! Enter a larger number")
            print()
    
print("You guessed the number in",{guesses},"guesses")
print()

print("Thanks for playing!")
print()
