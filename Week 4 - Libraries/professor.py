#In a file called professor.py, implement a program that:
#Prompts the user for a level, 𝑛. If the user does not input 1, 2, or 3, the program should prompt again.
#Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with 𝑛 digits. No need to support operations other than addition (+).
#Note: The order in which you generate x and y matters. Your program should generate random numbers in x, y pairs to simulate generating one math question at a time (e.g., x0 with y0, x1 with y1, and so on).
#Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem. If the user has still not answered correctly after three tries, the program should output the correct answer.
#The program should ultimately output the user’s score: the number of correct answers out of 10.
#Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3, and generate_integer returns a single randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:

import random


def main():
     get_level()


def get_level():
    levels = [1,2,3]
    x = []
    y = []

    values = 0

    while True:
        try:
            level = int(input("Level: "))
        
            if level in levels:
                while values < 10:
                    x.append(generate_integer(level))      
                    y.append(generate_integer(level))
                    values +=1

            else:
                raise ValueError
            math_problems(x, y)
            break
            
        except ValueError:  
            pass


def generate_integer(level):
    lower = 10**(level-1)
    upper = 10**level - 1
    return random.randint(lower, upper)

def math_problems(a, b):
    score = 0
    value = 0

    while value < 10:
        try:
            zr = a[value] + b[value]
            z = int(input(f"{a[value]} + {b[value]} = "))
            if zr == z:
                value +=1
                score +=1
            else:
                raise ValueError
        except ValueError:
            math_problems_error(a[value], b[value])
            value +=1
            pass
        
    print(f"Score: {score}")

def math_problems_error(a, b):
    value2 = 1
    while value2 < 3:
        try: 
            zr = a + b
            print("EEE")
            z = int(input(f"{a} + {b} = "))
            if zr == z:
                break
            else:
                raise ValueError

        except ValueError:
            value2 +=1
            pass

    if value2 >= 3:
        print(f"{a} + {b} = {zr}") 

if __name__ == "__main__":
    main()