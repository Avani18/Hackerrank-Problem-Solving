import math
import os
import random
import re
import sys

def julian(year):
    date = ''
    sum_day = 0
    days = {1:31, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    if year%4 == 0:
        days[2] = 29
    else:
        days[2] = 28
    
    for i in range(1,13):
        sum_day += days[i]
        if sum_day > 256:
            sum_day -= days[i]
            date += (str(256-sum_day)+'.')
            if i < 10:
                date += ('0'+str(i)+'.'+str(year))
                return date
            else:
                date += (str(i)+'.'+str(year))
                return date

def greg(year):
    date = ''
    sum_day = 0
    days = {1:31, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    
    if year == 1918:
        days[2] = 15
    elif year%400 == 0:
        days[2] = 29
    elif (year%4 == 0 and year%100 != 0):
        days[2] = 29
    else:
        days[2] = 28

    for i in range(1,13):
        sum_day += days[i]
        if sum_day > 256:
            sum_day -= days[i]
            date += (str(256-sum_day)+'.')
            if i < 10:
                date += ('0'+str(i)+'.'+str(year))
                return date
            else:
                date += (str(i)+'.'+str(year))
                return date


# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):

    if year <= 1917:
        return (julian(year))
    elif year >= 1918:
        return (greg(year))
    return 0


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()

