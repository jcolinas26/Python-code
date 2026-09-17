#In a file called shirtificate.py, implement a program that prompts the user for their name and outputs, using fpdf2, a CS50 shirtificate in a file called shirtificate.pdf similar to this one for John Harvard, with these specifications:
#The orientation of the PDF should be Portrait.
#The format of the PDF should be A4, which is 210mm wide by 297mm tall.
#The top of the PDF should say “CS50 Shirtificate” as text, centered horizontally.
#The shirt’s image should be centered horizontally.
#he user’s name should be on top of the shirt, in white text.

from fpdf import FPDF

def main():
    name = input("Name: ")

    pdf = FPDF(orientation="P", format="A4")   # make the object (Portrait, A4)
    pdf.add_page()                              # add a page to work on
    # ... call methods to add text and image ...
    pdf.image("shirtificate.png", x=(210 - 150) / 2, w=150)
    pdf.set_y(50)                          # move down to the chest (adjust this number)
    pdf.set_text_color(255, 255, 255)       # white
    pdf.set_font("helvetica", size=24)      # maybe bigger for the name
    pdf.cell(0, 10, name, align="C")
    #.....
    pdf.output("shirtificate.pdf")              # save it


if __name__ == "__main__":
    main()
