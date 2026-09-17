#In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY), otherwise known as middle-endian order, which is arguably bad design. Dates in that format can’t be easily sorted because the date’s year comes last instead of first. Try sorting, for instance, 2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program (e.g., a spreadsheet). Dates in that format are also ambiguous. Harvard was founded on September 8, 1636, but 9/8/1636 could also be interpreted as August 9, 1636!
#Fortunately, computers tend to use ISO 8601, an international standard that prescribes that dates should be formatted in year-month-day (YYYY-MM-DD) order, no matter the country, formatting years with four digits, months with two digits, and days with two digits, “padding” each with leading zeroes as needed.
#In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:
#Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again. Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.

def main():

    print(split_date())

def check_month(month_):
    month = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    x = 0
    for i in month:
        x+=1
        if i == month_:
            return x

    return 0


def split_date():

    while True:
        try:

            date = input("Date: ")

            if date[0].isdigit():#if date is in numeric format
                date_ = date.split("/")
                month = date_[0]
                day = date_[1]
                year = date_[2]

                if len(day) == 1:
                    day = "0" + day
                
                if int(day) < 1 or int(day) > 31:#checking days
                    raise ValueError

                if len(month) == 1:
                    month = "0" + month

                if int(month) < 1 or int(month) > 12:#checking months
                    raise ValueError

                return (year + "-" + month + "-" + day)

            else:#date format is September 8, 1636

                date_ = date.split(" ")
                month = date_[0]
                day = date_[1]
                day = day[:-1]#removing the , 
                year = date_[2]

                if len(day) == 1:
                    day = "0" + day

                if int(day) < 1 or int(day) > 31:#checking days
                    raise ValueError
                
                month2 = check_month(month)
                if month2 == 0:
                    raise ValueError
                else:
                    month3 = str(month2)
                    if len(month3) == 1:
                        month3 = "0" + month3            

        except (ValueError, IndexError):  
            pass



main()