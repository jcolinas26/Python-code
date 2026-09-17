#In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.

def main():
    mass = int(input("Enter mass: "))
    print("E: ", E(mass))

def E(mass):
    light = 300000000 * 300000000
    return mass * light

main()