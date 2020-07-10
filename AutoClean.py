import os
'''
This program is to count total lines in all the files on a given directory and subdirectories

'''

import glob
 
# Get a list of all the file paths that ends with .txt from in specified directory
fileList = glob.glob('C:/Users/JAtul/Downloads/*.ica')
 
# Iterate over the list of filepaths & remove each file.
for filePath in fileList:
    try:
        os.remove(filePath)
    except:
        print("Error while deleting file : ", filePath)