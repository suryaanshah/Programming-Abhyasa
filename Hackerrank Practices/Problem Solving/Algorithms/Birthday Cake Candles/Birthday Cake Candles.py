#!/bin/python3

import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):
    highest=max(candles) # Since we know all the heights of candles, we can know the maximum hight using the max function.
    num=0 # The no. of tallest candles.
    for i in candles: # 'i' is the iterator varaible. It's value is the value of the heights of candles. Eg. i is 6 cm in first round and then 8cm in next and it will take all the values the elements in the list 'candles'. So if it is the highests, we add 1 to num and if not, we continue.   
        if i == highest:
            num += 1
        else:
            continue
    return(num)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
