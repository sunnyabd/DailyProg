# code by Pan Sun Wei
import cProfile

# find first leap & last leap. number of leaps w/o exceptions = years/4
# find first and last year divisible by 100. number with exception1 = number w/o exception - (last-first)/100
# first first and last year that gives remainder of 200 & 600 when divided by 900.
# total = number1 - (number2 - number3 - number4)

# code results in constant worst case time complexity

def leaps(start=2019, end=2020):

    # worst case complexity O(4)
    for x in range(start, end):
        if x % 4 == 0:
            firstLeap4 = x
            break

    # worst case complexity O(4)
    for x in range(end-1, start-1, -1):
        if x%4 == 0:
            lastLeap4 = x
            break

    try:
        total4 = int(lastLeap4/4) - int(firstLeap4/4) + 1
    except:
        total4 = 0
        return total4

    # worst case complexity O(100)
    for x in range(start,end):
        if x%100 == 0:
            firstLeap100 = x
            break

    # worst case complexity O(100)
    for x in range(end-1, start-1, -1):
        if x%100 == 0:
            lastLeap100 = x
            break

    try:
        total100 = int(lastLeap100/100) - int(firstLeap100/100) + 1
    except:
        return total4

    # worst case complexity O(9)
    for x in range(int(firstLeap100/100),int(lastLeap100/100)+1):
        if x%9 == 2:
            firstLeap200 = x
            break

    # worst case complexity O(9)
    for x in range(int(lastLeap100/100),int(firstLeap100/100)-1,-1):
        if x%9 == 2:
            lastLeap200 = x
            break

    try:
        total200 = int(lastLeap200 / 9) - int(firstLeap200 / 9) + 1
    except:
        total200=0

    # worst case complexity O(9)
    for x in range(int(firstLeap100/100),int(lastLeap100/100)+1):
        if x%9 == 6:
            firstLeap600 = x
            break

    # worst case complexity O(9)
    for x in range(int(lastLeap100/100),int(firstLeap100/100)-1,-1):
        if x%9 == 6:
            lastLeap600 = x
            break

    try:
        total600 = int(lastLeap600 / 9) - int(firstLeap600 / 9) + 1
    except:
        total600=0

    return total4 - (total100 - total200 - total600)


# every 100 days julian loses 1 day except for the special cases.
# we find a year where julian calendar moves exactly 4 gregorian years due to this difference
# 365*4+1 = 1459 days

def bonus():
    year = 0
    diff = 0
    while True:
        year += 100
        diff -= 1
        if year%900 == (200 or 600):
            diff +=1
        if diff == -1459:
            return year

cProfile.run("print('Total number of leap years = {}'.format(leaps(123456789101112, 1314151617181920)))")
print("Total number of leap years = {}".format(leaps(2016, 2017)))
print("Total number of leap years = {}".format(leaps(2019, 2020)))
print("Total number of leap years = {}".format(leaps(1900, 1901)))
print("Total number of leap years = {}".format(leaps(2000, 2001)))
print("Total number of leap years = {}".format(leaps(2800, 2801)))
print("Total number of leap years = {}".format(leaps(123456, 123456)))
print("Total number of leap years = {}".format(leaps(1234, 5678)))
print("Total number of leap years = {}".format(leaps(123456, 7891011)))

cProfile.run("print(bonus())")


