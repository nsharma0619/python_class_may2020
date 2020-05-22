#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    level=0
    count=0
    valley=0
    for i in s:
        if(i=='U'):
            level+=1
        else:
            level-=1
        if(level<0):
            valley=1
        elif(valley==1 and level==0):
            count+=1
            valley=0
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
