# Python progam to iterate 
# over 3 lists using zip and izip function 
#itertools.zip_longest(*iterables, fillvalue=None)
#Make an iterator that aggregates elements from each of the iterables. If the iterables are of uneven length,
# missing values are filled-in with fillvalue. Iteration continues until the longest iterable is exhausted.

from itertools import zip_longest as zip
num = [1, 2, 3]
color = ['red', 'while', 'black'] 
value = [255, 256] 

# iterates over 3 lists and till all are exhausted 
for (a, b, c) in zip(num, color, value):
	print (a, b, c)
