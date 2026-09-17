while True:
    try:
        x = int(input("What is X: "))

    except ValueError:
        print("X is not an Integer")

    else:
        break

print(f"X is {x}")#you can use inside try/except the code that potentially can fail

while True:
    try:
        x = int(input("What is X: "))
        break

    except ValueError:
        pass #it will catch the expection but don´t show anything

print(f"X is {x}")#you can use inside try/except the code that potentially can fail