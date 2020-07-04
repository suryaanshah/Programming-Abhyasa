#!/bin/python3

import math
import os
import random
import re
import sys

N = int(input())

if N%2 == 0 and N>1 and N < 6:
    print("Not Weird")
elif N%2== 0 and N>5 and N<21:
    print("Weird")
elif N%2 ==0 and N > 20 :
    print("Not Weird")
else:
    print("Weird")
