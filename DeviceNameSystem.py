#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'deviceNamesSystem' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY devicenames as parameter.
#

def deviceNamesSystem(devicenames):
    # Write your code here
    dico={}
    result=[]

    for item in devicenames:
        if item in dico.keys():
            dico[item]+=1
            result.append(f"{item}{dico[item]}")
        else:
            dico[item]=0
            result.append(f"{item}")

if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    devicenames_count = int(input().strip())

    devicenames = []

    for _ in range(devicenames_count):
        devicenames_item = input()
        devicenames.append(devicenames_item)

    result = deviceNamesSystem(devicenames)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
