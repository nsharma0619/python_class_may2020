#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    lis_tmp=[]
    ans=[]
    for i in range(len(p)):
        lis_tmp.append(0)
        ans.append(0)
    for i in range(len(p)):
        lis_tmp[p[i]-1]=i+1
    for i in range(len(lis_tmp)):
        ans[p[i]-1]=lis_tmp[i]
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
