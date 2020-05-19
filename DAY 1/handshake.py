#!/bin/python3

import os
import sys

#
# Complete the handshake function below.
#
def handshake(n):
    #you can also use sum of AP formula and it is better to use
    count=0
    for i in range(n):
        count+=i
    return count
    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = handshake(n)

        fptr.write(str(result) + '\n')

    fptr.close()