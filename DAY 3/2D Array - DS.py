#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    ans=-63
    for i in range(0,4):
        for j in range(0,4):
            sum=0
            for k in range(j,j+3):
                sum+=arr[i][k]

            sum+=arr[i+1][j+1]

            for k in range(j,j+3):
                sum+=arr[i+2][k]

            if(sum>ans):
                ans=sum

    return ans




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()