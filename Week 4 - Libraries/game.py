#In a file called game.py, implement a program that:
#Prompts the user for a level, 𝑛. If the user does not input a positive integer, the program should prompt again.
#Randomly generates an integer between 1 and 𝑛, inclusive, using the random module.
#Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
#If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
#If the guess is larger than that integer, the program should output Too large! and prompt the user again.
#If the guess is the same as that integer, the program should output Just right! and exit.

import random

def main():
    while True:
        try:
            level = int(input("Level: "))

            if level <= 0:
                raise ValueError
            else:
                random_generator(level)
                break
    
        except ValueError:  
            pass


def random_generator(level_):
    numbrer = random.randint(1,level_) 

    while True:
        try:
            u_guess = int(input("Guess: "))
            if u_guess <= 0:
                raise ValueError
            else:
                if user_guess(u_guess, numbrer):
                    break

        except ValueError:
            pass

def user_guess(guess, randomn):
           
        if guess == randomn:
            print("Just Right!")
            return True
        elif guess < randomn:
            print("Too small!")
            return False
        else:
            print("Too large!")
            return False

main()