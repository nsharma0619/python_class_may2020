#!/bin/python3

import os
import sys
import math
#
# Complete the gameWithCells function below.
#
def gameWithCells(n, m):
    four=((n-n%2)*(m-m%2))//4
    two=math.ceil(((n%2)*m+(m%2)*n)//2)
    return four+two
    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    result = gameWithCells(n, m)

    fptr.write(str(result) + '\n')

    fptr.close()
