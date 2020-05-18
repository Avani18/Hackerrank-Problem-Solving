import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sumarr = sum(arr)
    mini = 9999999999999
    maxi = 0
    for i in range(5):
        newsum = sumarr - arr[i]
        mini = min(mini, newsum)
        maxi = max(maxi, newsum)

    print (mini, maxi)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

