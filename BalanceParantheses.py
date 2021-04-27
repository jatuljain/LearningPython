import math
import os
import random
import re
import sys

def getMin(s):
    # Write your code here
    op,cl = 0,0
    for i in range(s):
        if (s[j] == '('):
            op+=1
        else: # 
            cl+=1

    out = cl - op
    print(out) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = getMin(s)