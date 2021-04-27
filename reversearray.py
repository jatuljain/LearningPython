from array import *
'''
How to Sort the list inside array
'''

n = int(input("Enter the number of array element"))
arr = array('i')
for i in range(n):
    while True:
        try:
            val=int(input("Enter the next value"))
        except ValueError:
            print('PLease input a valid integer')
            continue
        break
    arr.append(val)

print(arr)

revarr = array('i',[])
for r in range(n):
    revarr.append(arr[n-r-1])


print(revarr)