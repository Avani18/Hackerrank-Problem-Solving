import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

from math import gcd
from functools import reduce

def getTotalX(a, b):
    # Write your code here
    lcm = reduce(LCM, a, 1)
    gcdd = reduce(gcd, b)

    lcm_copy = lcm

    count = 0
    while lcm <= gcdd:
        if(gcdd % lcm) == 0:
            count += 1
        lcm = lcm + lcm_copy

    return count
    
def LCM(a, b):
    return (a*b)//gcd(a,b)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
