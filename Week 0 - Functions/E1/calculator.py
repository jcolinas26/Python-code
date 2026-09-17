#x = input("What´s X? ")
#y = input("What´s Y? ")

#z = int(x) + int(y) #input creates strings so we need to convert them to int

#print(z)

#x = int(input("What´s X? "))
#y = int(input("What´s Y? "))

#print(x+y)

#float for decimal values
#x = float(input("What´s X? "))
#y = float(input("What´s Y? "))

#print(x+y)
#print(round(x+y))#round a decimal number to the closest int

#z = x+y
#print(f"{z:,}")#print numbers like 1,000 instead of 1000

######

def main():
    x = int(input("What´s X? "))
    print("x squared is ", square(x))

def square(n):
    return n * n #return values to the calling function

main()

