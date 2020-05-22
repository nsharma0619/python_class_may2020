#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternate function below.
def alternate(s):
    st=set()
    for i in s:
        st.add(i)
    st=list(st)
    st.sort()
    lis=[]
    for i in range(len(st)-1):
        for j in range(i+1,len(st)):
            lis.append([st[i],st[j]])
    max_str_len=0
    for i in lis:
        ans_str=""
        for j in s:
            if(j in i):
                ans_str+=j
        alter=1
        for k in range(len(ans_str)-1):
            if(ans_str[k]==ans_str[k+1]):
                alter=0
        if(alter==1 and len(ans_str)>max_str_len):
            max_str_len=len(ans_str)
    return max_str_len

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
