#! python3
# detects dates in a standard format and validates for real/fake days

import re

dateRegex = re.compile(r'''(
    (\d{2})
    (\/)
    (\d{2})
    (\/)
    (\d{4})
    )''', re.VERBOSE)

def dateDetect(dateIn):
    dateObject = dateRegex.search(dateIn)
    day = int(dateObject.group(2))
    month = int(dateObject.group(4))
    year = int(dateObject.group(6))

    success = dateObject.group(0) + ' is a valid date'
    failDay = 'Day out of range'
    failMon = 'Month out of range'
    failYr = 'Year out of range'

    if year > 1000 and year < 2999:
        if month > 0 and month < 13:  # 12 months in a year
            if month == 4 or month == 6 or month == 9 or month == 11:       # Checks for Apr, Jun, Sept, and Nov
                if day > 0 and day < 31:                                    # Which have 30 days
                    print(success)
                else:
                    print(failDay)
            if month == 2 and year % 4 == 0:                                # Checks for Feb in leap years
                if day > 0 and day < 30:                                    # When Feb has 29 days
                    print(success)
                else:
                    print(failDay)
            if month == 2 and year % 4 != 0:                                # Checks for Feb in non-leap years
                if day > 0 and day < 29:                                    # When feb has 28 days
                    print(success)
                else:
                    print(failDay)
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:   # Catches all other valid months
                if day > 0 and day < 32:                                    # When months have 31 days
                    print(success)
                else:
                    print(failDay)
        else:
            print(failMon)
    else:
        print(failYr)

while True:
    print('Enter a date using the format dd/mm/yyyy')
    userInput = str(input())
    dateDetect(userInput)
