#!/bin/python3

import os
import sys

#
# Complete the primeCount function below.
#
def primeCount(n):
    prime_arr=[ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    mul=1
    i=0
    while(mul*prime_arr[i]<=n):
        mul*=prime_arr[i]
        i+=1
    return i
    #
    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = primeCount(n)

        fptr.write(str(result) + '\n')

    fptr.close()
