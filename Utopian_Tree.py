import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    i = 1
    ht = 1
    while (i <= n):
        if i%2 == 0:
            ht += 1
            i += 1
        else:
            ht *= 2
            i += 1
    return ht
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
