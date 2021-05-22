#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(1, n+1): # start with i=1, end when reached n+1
        print((" "*(n-i)) + ("#"*(n-(n-i)))) # Gives <space> n-i times, and then gives '#' n-(n-i) times.

if __name__ == '__main__':
    n = int(input())

    staircase(n)
