#Data, too, often needs to be “cleaned,” as by reformatting it, so that values are in a consistent, if not more convenient, format. Consider, for instance, this CSV file of students, before.csv, below:
#Even though each “row” in the file has three values (last name, first name, and house), the first two are combined into one “column” (name), escaped with double quotes, with last name and first name separated by a comma and space. Not ideal if Hogwarts wants to send a form letter to each student, as via mail merge, since it’d be strange to start a letter with:
#Dear Potter, Harry,
#Rather than with, for instance:
#Dear Harry,
#In a file called scourgify.py, implement a program that:
#Expects the user to provide two command-line arguments:
#the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
#the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
#Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name.
#If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an error message.

import sys
import csv

def main():
    if len(sys.argv) != 3:
        sys.exit("Incorrect number of arguments")
    else:
        open_file(sys.argv[1], sys.argv[2])

def open_file(file_in, file_out):
    try:
       if not file_in.endswith(".csv") and not file_out.endswith(".csv"):
           raise ValueError
       else:
           with open(file_in, "r") as file:
               file_input(file)
    except ValueError:
        sys.exit("File extension not valid")
    except FileNotFoundError:
        sys.exit("File not found")

def file_input(fin):
    students = []
    reader = csv.DictReader(fin)
    for row in reader:
        students.append({"name": row["name"], "house": row["house"]})

    changes(students)

def file_output(fout):
    with open("after.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "house"])
        for student in fout:
            writer.writerow({"name": student["name"], "house": student["house"]})


def changes(students_):
    students_new = []

    for student in students_:
        full_name = student["name"].split(",")
        name = full_name[1]
        surname = full_name[0]
        new_name = f"{name}, {surname}".strip()
        students_new.append({"name": new_name, "house": student["house"]})

    file_output(students_new)
    
if __name__ == "__main__":
    main()
