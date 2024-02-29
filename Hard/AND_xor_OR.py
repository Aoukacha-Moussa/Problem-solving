#!/bin/python3

import math
import os
import random
import re
import sys

def andXorOr(a):
    # Write your code here
    lis_max=[]
    max_A = 0
    for x in range(len(a)):
        while lis_max:
            res=lis_max[-1] ^ a[x]
            max_A=max(max_A, res)
            if lis_max[-1]>a[x]:
                lis_max.pop()
            else:
                break
        lis_max.append(a[x])            
    return max_A

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = andXorOr(a)

    fptr.write(str(result) + '\n')

    fptr.close()
