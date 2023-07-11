import os
'''
This program is to count total lines in all the files on a given directory and subdirectories

'''

import glob
 
# Get a list of all the file paths that ends with .txt from in specified directory
fileList = glob.glob('C:/Users/atul.jain/Downloads/*.ica')
 
# Iterate over the list of filepaths & remove each file.
for filePath in fileList:
    try:
        os.remove(filePath)
    except:
        print("Error while deleting file : ", filePath)

#This is 2ndbranch 1st commit.
#This is 2ndbranch 2nd commit.
#This is 2ndbranch 3rd commit.