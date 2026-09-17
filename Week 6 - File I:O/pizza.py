#In a file called pizza.py, implement a program that expects exactly one command-line argument, the name (or path) of a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII art using tabulate, a package on PyPI at pypi.org/project/tabulate. Format the table using the library’s grid format. If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .csv, or if the specified file does not exist, the program should instead exit via sys.exit.

import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) != 2:
        sys.exit("Incorrect number of arguments")
    else:
        open_file(sys.argv[1])

def open_file(file_):
    try:
       if not file_.endswith(".csv"):
           raise ValueError
       else:
           with open(file_, "r") as file:
               print_menu(file)
    except ValueError:
        sys.exit("File extension not valid")
    except FileNotFoundError:
        sys.exit("File not found")


def print_menu(fp):
    pizza = []
    
    reader = csv.reader(fp)

    for row in reader:
        pizza.append(row)

    print(tabulate(pizza, headers="firstrow", tablefmt="grid"))

if __name__ == "__main__":
    main()