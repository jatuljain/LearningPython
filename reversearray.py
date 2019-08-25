from array import *

n = int(input("Enter the number of array element"))
arr = array('i',[])
for i in range(n):
    val=int(input("Enter the next value"))
    arr.append(val)

print(arr)

revarr = array('i',[])
for r in range(n):
    revarr.append(arr[n-r-1])


print(revarr)