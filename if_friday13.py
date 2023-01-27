# Create a function in Python that accepts two parameters.
# They’ll both be numbers.
# The first will be the month as a number, and the second will be the four-digit year.

# The function should parse the parameters
# and return True if the month contains a Friday the 13th and False if it doesn’t.

import calendar


def isfriday13(year, month):
    print(f"Provided year and month: {year}, {month}")
    x = calendar.Calendar(0)
    lst = x.monthdays2calendar(year=year, month=month)
    counter = 0
    for week in lst:
        for el in week:
            if el[0] == 13 and el[1] == 4:
                return "Yes, this month has a Friday the 13th"
            else:
                counter += 1

    if counter:
        return "No, this month doesn't have a Friday the 13th"


var = True
count = 0
year = 0
month = 0
while year not in [x for x in range(1800, 2101)] and month not in [x for x in range(1, 13)]:
    if count != 0:
        print("""Year must be in 1800 - 2100 and month must be in 1 - 12.
              Try again, please""")
    try:
        year = int(input("Enter a year:"))
        month = int(input("Enter a month:"))
    except:
        print("Write good numbers, please")
    count += 1

print(isfriday13(year, month))

