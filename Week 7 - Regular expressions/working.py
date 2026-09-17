#In a file called working.py, implement a function called convert that expects a str in any of the 12-hour formats below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00). Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space before each. Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.
#9:00 AM to 5:00 PM
#9 AM to 5 PM
#9:00 AM to 5 PM
#9 AM to 5:00 PM
#Raise a ValueError instead if the input to convert is not in either of those formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that someone’s hours will start ante meridiem and end post meridiem; someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).
#Structure working.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit, but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.
#import re
#import sys
#def main():
#    print(convert(input("Hours: ")))
#def convert(s):
#    ...
# ...
#if __name__ == "__main__":
#    main()

import re
import sys


def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
            sys.exit("Invalid format")

def convert(s):
        if matches := re.search(r"^(1[0-2]|[1-9])(?::([0-5][0-9]))? (AM|PM) to (1[0-2]|[1-9])(?::([0-5][0-9]))? (AM|PM)$", s):
            hour1 = int(matches.group(1))
            hour2 = int(matches.group(4))
            minutes1 = int(matches.group(2)) if matches.group(2) else 0
            minutes2 = int(matches.group(5)) if matches.group(5) else 0

            if matches.group(3) == "PM" and hour1 != 12:
                hour1 = hour1 + 12
            elif matches.group(3) == "AM" and hour1 == 12:
                hour1 = 0

            if matches.group(6) == "PM" and hour2 != 12:
                hour2 = hour2 + 12
                
            elif matches.group(6) == "AM" and hour2 == 12:
                hour2 = 0

            return f"{hour1:02}:{minutes1:02} to {hour2:02}:{minutes2:02}"
        
        raise ValueError

    

if __name__ == "__main__":
    main()  

