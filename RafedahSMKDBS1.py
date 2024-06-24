#!/usr/bin/env python

import random

def main():
    """Start My Favourite Colour Guessing Game."""
    print("Guess my favourite colour!. You are given 3 trials")
    
    favcolour = [
        "blue",
        "pink",
        "gold",
        "nude",
        "grey"
        ]
 #Choice of colors given to the players   
    print(favcolour)

    x = "pink"
    max_trials= 3
    trial=0
    guess = None
    #print(x)
    while trial<max_trials:
        guess = str(input("What is my favourite colour?: "))
        max_trials -= 1
        if x == guess:
            print(f"You guessed.Congratulations you got it right!".format(guess))
            break
        else:
            print(f"Unfortunately you got the wrong answer.".format(guess))
            print(f"You have {max_trials} chances remaining.")
           
        if max_trials == 0:
            print(f"out of attempts. My favourite color is actually {x}.".format(guess))
        
main()