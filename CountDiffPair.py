# A simple program to count pairs with difference d 


def countpairswithdiffk(array, leng, d):
	count = 0
	
	# Pick all elements one by one 
	for a in range(0, leng): 
		
		# See if there is a pair of this picked element 
		for b in range(a+1, leng) : 
			
			if array[a] - array[b] == d or array[b] - array[a] == d: 
				count += 1
				
	return count 


# Driver program 
array = [1, 5, 3, 4, 2] 

leng = len(array) 
d = 3
print ("Count of pairs with given diff is ", countpairswithdiffk(array, leng, d))
