# This one is to count number of ascii character in string.
import string

str = "This is the string to check for now this has 40 total"


def countascii (str):
    count = 0
    for char in str:
        if char in string.ascii_letters:
            count = count+1
    return count


if __name__ == "__main__" :
    print(countascii(str))

