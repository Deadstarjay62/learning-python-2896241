# Solution to programming challenge for Learning Python course
# LinkedIn Learning Python course by Joe Marini
#

import calendar

# This function counts the number of the given weekday for the
# specified year and month and returns the result
def countdays(theyear, themonth, whichday):
    weekslist = calendar.monthcalendar(theyear, themonth)
    return sum(1 for week in weekslist if week[whichday] != 0)


print("--Day counter program--\n")

run = True
while run:
    try:
        print("Which day of the week do you want to count?")
        print("0: Monday")
        print("1: Tuesday")
        print("2: Wednesday")
        print("3: Thursday")
        print("4: Friday")
        print("5: Saturday")
        print("6: Sunday")
        print("Or 'exit' to quit")

        theday = input("? ")
        if theday == "exit":
            run = False
            break
        day = int(theday)

        yearstr = input("Enter year: ")
        year = int(yearstr)

        monthstr = input("Enter month: ")
        month = int(monthstr)

        result = countdays(year, month, day)
        print(f"There are {str(result)} of those days in the month and year specified")
        print("-----------\n")
    except Exception as e:
        print(e)
        print("Sorry, that's not valid input")

