import os
import re
opencurly = []
Closecurly = []


def countspecialchar(schar, filename):
    fh = open(filename)
    content = fh.read()
    countchar = re.findall(schar, content)
    # print(countchar)
    countcharlen = len(countchar)
    fh.close()
    return countchar, countcharlen


if __name__ == "__main__":
    opencurlylist, finalcountopencurly = \
        countspecialchar('{', "E:\\Python\\test.txt")
    # print("\n final list opencurly {  :", opencurlylist)
    # print("\n finalcountopencurly {  :", finalcountopencurly)
    closecurlylist, finalcountclosecurly = \
        countspecialchar('}', "E:\\Python\\test.txt")
    # print("\n final list closecurly {  :", closecurlylist)
    # print("\n finalcountclosecurly }  :", finalcountclosecurly)


for (openc, closec) in zip(opencurlylist, closecurlylist):
    i = 0
    print(openc, closec)
    if openc == '{' and closec != '}':
        print("braces not matching")
    else:
        print("braces are matching")
        i = i + 1

    if i != len(opencurlylist) | i != len(closecurlylist):
        print("braces not matched in numbers")
        break
