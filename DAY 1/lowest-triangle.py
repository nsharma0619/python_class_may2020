#!/bin/python3

import sys
import math
def lowestTriangle(base, area):
    height=2*area/base
    height=math.ceil(height)
    return height
    # Complete this function

base, area = input().strip().split(' ')
base, area = [int(base), int(area)]
height = lowestTriangle(base, area)
print(height)
