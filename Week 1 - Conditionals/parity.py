#x = int(input("What´s X: "))

#if x % 2 == 0:
#    print("Even")
#else:
#    print("Odd")

def main():
    x = int(input("What´s X: "))

    if is_even(x):
       print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
         return True   
    else:
        return False
    
    #other option: return True if n % 2 == 0: else False
    #other option: return n % 2 == 0
main()