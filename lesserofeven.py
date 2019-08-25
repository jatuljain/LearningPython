'''
Funcion to check lesser digit out of given two
'''
def lesser_of_two_even(first, second):
    '''
    Funcion to check lesser digit out of given two
    '''
    if first % 2 == 0 and second % 2 == 0:
        if first < second:
            return first
        else:
            return second
    elif first % 2 != 0 or second % 2 != 0:
        if first < second:
            return second
        else:
            return first
    else:
        pass
FINALVALUE = lesser_of_two_even(2, 4)
print(FINALVALUE)
