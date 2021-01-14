#!/bin/python3

import sys

def timeConversion(s):
    # Complete this function
    amOrPm = s[-2:]
    toReturn = ""

    if(amOrPm == "PM"):
        if(int(s[0:2]) < 12):
            toReturn = toReturn + str(12 + int(s[0:2])) + s[2:-2]
        else:
            toReturn = toReturn + str(int(s[0:2])) + s[2:-2]
    else:
        if(s[0:2] == '12'):
            toReturn = toReturn + "00" + s[2:-2]
        else:
            toReturn = toReturn + s[:-2]

    return toReturn
s = input().strip()
result = timeConversion(s)
print(result)
