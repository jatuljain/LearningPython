'''
Finding a unique values in list
'''

# testlist = [2, 3, 4, 5, 4, 3, 2, 100]
# print (testlist)
# print ("\n")
#
# newlist = []
# for l in testlist:
# 	if l not in newlist:
# 		newlist.append(l)
# print (newlist)
#
#
# ### or simply use set
# uni = set(testlist)
# print ("Unique list from set \t", uni)    ### Unique list from set 	 {2, 3, 100, 4, 5}
# print("sorted Unique list from set \t", sorted(uni))  ## [2, 3, 4, 5, 100]
'''

############################################################################################################

#--------------------------------------------
# To check the reference of a variable use "id"
#--------------------------------------------
x=10
y=x

if (id(x)==id(y)):
	print ("x and y are having same ref")
	
#----------------------------------------------------------------------------------------------------------
'''

### Title method title() returns a copy of the string in which first characters of all the words are capitalized.	
# string = "this is ATUL Jain"
# print (string.title())  ### This Is Atul Jain
############

#
# numericstring = "1234"
# print (numericstring.isdecimal())  ### True


L = [1, 2, 5, 10, -10]
print (L) 	 		## [1, 2, 5, 10, -10]
print (max(L))      ## 10
print (L.index(2))  ## 1, index means position of that value 2
L.remove(2)
print (L) 			## [1, 5, 10, -10]
L.reverse()
print (L) 			## [-10, 10, 5, 1]
L.sort()
print (L) 			## [-10, 1, 5, 10]




