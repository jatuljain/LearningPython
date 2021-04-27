import copy

####################################################################
# Best link to read this --> https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/
# In Python, Assignment statements do not copy objects, they create bindings between a target and an object.
# When we use = operator user thinks that this creates a new object; well, it doesn’t. It only creates a new variable
# that shares the reference of the original object. Sometimes a user wants to work with mutable objects, in order to do
# that user looks for a way to create “real copies” or “clones” of these objects. Or, sometimes a user wants copies
# that user can modify without automatically modifying the original at the same time, in order to do that we create
# copies of objects.
#
# A copy is sometimes needed so one can change one copy without changing the other. In Python, there are two ways to
# create copies :
#
# Deep copy
# Shallow copy

# Important Points:
# The difference between shallow and deep copying is only relevant for compound objects (objects that contain
# other objects, like lists or class instances):
#
# A shallow copy constructs a new compound object and then (to the extent possible) inserts references into
# it to the objects found in the original.
# A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects
# found in the original.
###################################################################

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

######################
###Output Changing only in new variable
######################
########  --> simplelist 1 out put with deep copy [1, 2, 3, 4, 5]
########  --> newlist 2 out put with deep copy ['updated', 2, 3, 4, 5]



newlist = copy.copy(simplelist)

newlist[0] = "newupdate"

print ("simplelist 1 out put with shallow copy", simplelist)
print ("newlist 2 out put with shallow copy", newlist)
######################
###Output Changing even in original variable
######################
###### --> simplelist 1 out put with shallow copy [1, 2, 3, 4, 5]
###### --> newlist 2 out put with shallow copy ['newupdate', 2, 3, 4, 5]
