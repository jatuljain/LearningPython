mylist = [1,2,3,4,5,6,23,343,454,45]
print(mylist)
myoddlist = []
myevenlist = []

for num in mylist:
    if num % 2 == 0:
        myevenlist.append(num)
    else:
        myoddlist.append(num)

print(myevenlist)
print(myoddlist)

myevenlist.sort()
myoddlist.sort()
#
bigeven = myevenlist[-1]
bigodd = myoddlist[-1]

print("biggest even : ", bigeven)
print("biggest odd :" , bigodd)
