
import math
import os
import random
import re
import sys


def solve(arr, queries):
    min_lis=[]
    for x in queries:
        max_lis=[]
        for y in range(len(arr)-x+1):
            sub=arr[y:y+x]
            max_lis.append(max(sub))
        min_lis.append(min(max_lis))
    return min_lis
            
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = solve(arr, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
