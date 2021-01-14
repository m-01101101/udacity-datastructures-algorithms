# TODO
def daysBetweenDates_(year1, month1, day1, year2, month2, day2):
    # Coarse grain approach
    """
    Calculates the number of days between two dates.
    """
    # assert date2 greater than date1

    # assert valid dates (ie no 31st June)
    yeardays = (year2 - year1) * 365.25

    monthdays = (month2 - month1) * 30.4

    daydays = day2 - day1

    return int(yeardays) + int(monthdays) + int(daydays)


def testDaysBetweenDates():

    # test same day
    assert daysBetweenDates_(2017, 12, 30, 2017, 12, 30) == 0
    # test adjacent days
    assert daysBetweenDates_(2017, 12, 30, 2017, 12, 31) == 1
    # test new year
    assert daysBetweenDates_(2017, 12, 30, 2018, 1, 1) == 2
    # test full year difference
    assert daysBetweenDates_(2012, 6, 29, 2013, 6, 29) == 365

    print("Congratulations! Your daysBetweenDates")
    print("function is working correctly!")


testDaysBetweenDates()

####################################################################


def isLeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def daysInMonth(year, month):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4, 6, 9, 11):
        return 30
    elif isLeapYear(year) and month == 2:
        return 29
    elif not isLeapYear(year) and month == 2:
        return 28


# Using a helper functions
def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1


def daysBetweenDates__(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
    and year2/month2/day2. Assumes inputs are valid dates
    in Gregorian calendar, and the first date is not after
    the second."""
    days = 0
    mydate = (year1, month1, day1)
    while mydate != (year2, month2, day2):
        mydate = nextDay(*mydate)
        days += 1
    return days


def test():
    test_cases = [
        ((2012, 9, 30, 2012, 10, 30), 30),
        ((2012, 1, 1, 2013, 1, 1), 360),
        ((2012, 9, 1, 2012, 9, 4), 3),
    ]

    for (args, answer) in test_cases:
        result = daysBetweenDates__(*args)
        if result != answer:
            print(f"Test with data:", {args}, "failed")
        else:
            print("Test case passed!")


test()


def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
    and year2/month2/day2. Assumes inputs are valid dates
    in Gregorian calendar."""
    # program defensively! # using helper function as assertion
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    if year1 % 4 == 0:
        "do something because it's a leap year"
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days


def test():
    test_cases = [
        ((2012, 1, 1, 2012, 2, 28), 58),
        ((2012, 1, 1, 2012, 3, 1), 60),
        ((2011, 6, 30, 2012, 6, 30), 366),
        ((2011, 1, 1, 2012, 8, 8), 585),
        ((1900, 1, 1, 1999, 12, 31), 36523),
    ]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print(f"Test with data:", {args}, "failed")
        else:
            print("Test case passed!")


test()
