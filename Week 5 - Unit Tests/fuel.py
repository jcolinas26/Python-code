#Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.
#In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein X is a non-negative integer and Y is a positive integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.
#If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError

def main():
    fr = input("fraction: ")
    convert(fr)
    print(fr)


def convert(fraction):
    try:
        frac = fraction.split("/")
        x = int(frac[0])
        y = int(frac[1])
        if x > y:
            raise ValueError
        if y == 0:
            raise ZeroDivisionError
        
        z = round(x / y * 100)
        return z
                
    except (ValueError, ZeroDivisionError):
        return "Error"

def gauge(percentage):
    if 1 < percentage < 99:
        return f"{percentage}%"
    elif percentage <= 1:
        return "E"
    else:
        return "F"


if __name__ == "__main__":
    main()