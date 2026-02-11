import os

def getMin(s):
    op, cl = 0, 0

    for ch in s:
        if ch == '(':
            op += 1
        else:
            cl += 1

    return abs(cl - op)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    result = getMin(s)

    fptr.write(str(result) + '\n')
    fptr.close()
