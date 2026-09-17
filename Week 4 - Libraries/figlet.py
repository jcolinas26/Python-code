#FIGlet, named after Frank, Ian, and Glen’s letters, is a program from the early 1990s for making large letters out of ordinary text, a form of ASCII art:
#Among the fonts supported by FIGlet are those at figlet.org/examples.html.
#FIGlet has since been ported to Python as a module called pyfiglet.
#In a file called figlet.py, implement a program that:
#Expects zero or two command-line arguments:
#Zero if the user would like to output text in a random font.
#Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
#Prompts the user for a str of text.
#Outputs that text in the desired font.
#If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message.#


from pyfiglet import Figlet
import random
import sys

def main():
    if len(sys.argv) > 3:
        sys.exit("Too many arguments")
    elif len(sys.argv) == 2:
        sys.exit("Incorrect number of arguments")

    user_input = input("Input: ")

    if len(sys.argv) == 1:
        random_output(user_input)#no arguments
    else:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            user_output(user_input, sys.argv[2])#2 arguments
        else:
            sys.exit("Incorrect arguments")

def random_output(inp):
    figlet = Figlet()
    figlet_list = figlet.getFonts()

    font_ = random.choice(figlet_list) 
    figlet.setFont(font=font_)
    print(figlet.renderText(inp))

def user_output(inp, font_):
    figlet = Figlet()
    figlet_list = figlet.getFonts()

    if font_ in figlet_list:
        figlet.setFont(font=font_)
        print(figlet.renderText(inp))
    else:
        sys.exit("Not valid font")

   
main()

