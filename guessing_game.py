"""
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
"""

import random

def start_game():

    secret_number = random.randint(1, 10)
    guesses = 0
    
    print("Hello friend! Let's play a game.")
    
    while True:
        try:
            guess = int(input("I'm thinking of a number between 1 and 10. Can you guess what it is?  "))
        except ValueError:
            print("{} isn't a number. Please try again.".format(guess))
        else:
            if guess == secret_number:
                guesses += 1
                print("Smarty pants! You guessed it. My number was {}. It only took you {} guesses.".format(secret_number, guesses))
                break
            elif guess < secret_number:
                guesses += 1
                print("Sorry, my number is higher than {}. Try again.".format(guess))
            else:
                guesses += 1
                print("My number is lower than {}. Try again.".format(guess))
            
start_game()