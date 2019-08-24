import copy

########### Example with list of list.
######################
li1 = [1, 2, [3, 4], 5]

######################
#### Deep copy exp
######################
li2 = copy.deepcopy(li1)

li2[2][0] = 7

print ("list 1 out put with deep copy", li1)
print ("list 2 out put with deep copy", li2)

######################
###Output Changing only in new variable
######################
####  --> list 1 out put with deep copy [1, 2, [3, 4], 5]
####  --> list 2 out put with deep copy [1, 2, [7, 4], 5]

######################
#### Shallow copy exp
######################
li2 = copy.copy(li1)
li2[2][0] = 9

print ("list 1 out put with Shallow copy", li1)
print ("list 2 out put with Shallow copy", li2)
######################
###Output Changing even in original variable
######################
####  --> list 1 out put with Shallow copy [1, 2, [9, 4], 5]
####  --> list 2 out put with Shallow copy [1, 2, [9, 4], 5]

##############################################################################################################
########### Example with simple list.
##############################################################################################################
simplelist = [1,2,3,4,5]

newlist = copy.deepcopy(simplelist)

newlist[0] = "updated"

print ("simplelist 1 out put with deep copy", simplelist)
print ("newlist 2 out put with deep copy", newlist)


newlist = copy.copy(simplelist)

newlist[0] = "newupdate"
print ("simplelist 1 out put with shallow copy", simplelist)
print ("newlist 2 out put with shallow copy", newlist)















