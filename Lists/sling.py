#### ###################################
# Get the 2nd largest number in the list
########################################

# Python program to find second largest
# number in a list

# list of numbers - length of list should be at least 2
list1 = [10, 20, 4, 45, 99]

mx=max(list1[0],list1[1])
secondmax=min(list1[0],list1[1])
n =len(list1)
for i in range(2,n):
	if list1[i]>mx:
		secondmax=mx
		mx=list1[i]
	elif list1[i]>secondmax and mx != list1[i]:
		secondmax=list1[i]
	else:
		if secondmax == mx:
			secondmax = list1[i]

print("Second highest number is method 1: ",str(secondmax))

# -----------------------------------------------------------------------------------
# Python program to find second largest
# number in a list

# list of numbers
list1 = [10, 20, 64, 45, 99]

# new_list is a set of list1
new_list = set(list1)

# removing the largest element from temp list
new_list.remove(max(new_list))

# elements in original list are not changed
# print(list1)

print("Second highest number is method 2: ", max(new_list))





# -----------------------------------------------------------------------------------

# Python program to find second largest
# number in a list

# list of numbers
list1 = [10, 20, 4, 450, 99]

# new_list is a set of list1
new_list = set(list1)

# removing the largest element from temp list
new_list.remove(max(new_list))

# elements in original list are not changed
# print(list1)

print("Second highest number is method 3: ",max(new_list))

# ------------------------------------------------------------------------------------
def getlar(arr):
    lar = 0;
    for i in arr:
        # print("lar is ", lar)
        # print("i is ", i)
        if lar <= i:
            lar = i
    return lar

def getseclar(arr):
    lar = 0;
    seclar = 0;
    for i in arr:
        if lar <= i:
            lar = i

    arr.remove(lar)
    for i in arr:
        if seclar <= i:
            seclar = i
    return seclar


arr = [3,5, 10, 4]

print(arr)
largetst = getlar(arr)
seclargetst = getseclar(arr)

print("largest is", largetst)
print("seclargest is", seclargetst)

# ------------------------------------------------------------------------------------