#!/bin/python3

import math
import os
import random
import re
import sys


def truckTour(petrolpumps):
    total_petrol = 0
    total_deficit = 0
    start_index = 0
    
    for i in range(len(petrolpumps)):
        petrol, distance = petrolpumps[i]
        total_petrol += petrol
        total_petrol -= distance
        if total_petrol < 0:
            start_index = i + 1
            total_deficit += total_petrol
            total_petrol = 0

    return start_index
          
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
