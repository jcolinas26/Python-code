#In a file called plates.py, reimplement Vanity Plates from Problem Set 2, restructuring your code per the below, wherein is_valid still expects a str as input and returns True if that str meets all requirements and False if it does not, but main is only called if the value of __name__ is "__main__":
#def main():
#    ...
#def is_valid(s):
#    ...
# if __name__ == "__main__":
#    main()
#Then, in a file called test_plates.py, implement four or more functions that collectively test your implementation of is_valid thoroughly, each of whose names should begin with test_ so that you can execute your tests with:
#pytest test_plates.py


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if not plate_long(s):
        return False
    if not start_letter(s):
        return False
    if not no_punctuation(s):
        return False
    if not numbers_at_end(s):
        return False

    return True
    

def start_letter(s):

    if s[0].isalpha() and s[1].isalpha():
        return True

    return False

def plate_long(s):

    return 2 <= len(s) <= 6

def no_punctuation(s):
    for i in s:
        if not i.isalnum():
            return False
        
    return True

def numbers_at_end(s):

    for i in range(len(s)):
            if s[i].isnumeric():
                if s[i] == "0":
                    return False
                else:
                    if s[i:].isdigit():
                        return True #[i:] means from the current position till end
                    else:
                        return False
    
    return True

if __name__ == "__main__":
    main()