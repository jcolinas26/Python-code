def main():
    print_column(3)
    print_row(4)
    print_square(3)


def print_column(h):
    for _ in range(h):
        print("#")

def print_row(w):
    print("?" * w)


def print_square(s):
    for i in range(s):#for every row
        for j in range(s):#for every brick
            print("#", end="")
        print()


main()

