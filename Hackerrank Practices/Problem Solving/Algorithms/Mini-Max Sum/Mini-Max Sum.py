#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sumofall = sum(arr)
    minim = sumofall - max(arr)
    maxim = sumofall - min(arr)
    print(minim, maxim)
# If we subtract the max value with sum, we get the min value.
# If we subtract the min value with the sum, we get the max value.
    
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
