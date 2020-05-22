#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    ans=[]
    for i in range(len(arr)+1):
        ans.append(0)
    for i in arr:
        ans[i]+=1
    n=max(ans)
    for i in range(len(ans)):
        if(ans[i]==n):
            break
    return i

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
