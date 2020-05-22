#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    number=1
    upper=1
    lower=1
    spcl=1
    for i in password:
        if(i in "0123456789"):
            number=0
        elif(i in "abcdefghijklmnopqrstuvwxyz"):
            upper=0
        elif(i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            lower=0
        else:
            spcl=0

    if(len(password)>=6):
        return number+upper+lower+spcl
    else:
        numberOfWords=6-len(password)
        bounded=number+upper+lower+spcl
        if(numberOfWords>=bounded):
            return numberOfWords
        else:
            return bounded

    # Return the minimum number of characters to make the password strong

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
