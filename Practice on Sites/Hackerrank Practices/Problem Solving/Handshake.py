#!/bin/python3

import os
import sys

#
# Complete the handshake function below.
#
def handshake(n):
    #
    # Write your code here.
    #
    for i in range(t):
        return(int(n*(n-1)/2))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = handshake(n)

        fptr.write(str(result) + '\n')

    fptr.close()
