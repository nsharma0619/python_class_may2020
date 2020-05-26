#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    arr.sort()
    ans=[len(arr)]
    while(len(arr)!=0):
        min_element=min(arr)
        for i in range(len(arr)):
            arr[i]=arr[i]-min_element
        while(0 in arr):
            arr.pop(0)
        if(len(arr)>0):
            ans.append(len(arr))
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
