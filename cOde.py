#!/bin/python3

import math
import os
import random
import re
import sys

def flatlandSpaceStations(n, c):  
    c.sort()
    MaxDistance=max(c[0],n-1-c[len(c)-1])
    for j in range(1,len(c)):
        dis=abs(c[j]-c[j-1])
        if dis>1:
            dis=dis//2
            if dis>MaxDistance:
                MaxDistance=dis  
    return(MaxDistance)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
