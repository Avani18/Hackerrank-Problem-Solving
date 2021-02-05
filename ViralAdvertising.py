import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    if n == 1:
        return 2

    tot_likes = 2
    likes_day = 2
    for i in range(2,n+1):
        likes_day = math.floor((likes_day*3)/2)
        tot_likes += likes_day
        
    return tot_likes
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
