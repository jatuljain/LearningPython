"""
This program is to count total lines in all the files on a 
given directory and subdirectories

"""
from os import *

# import os
import glob

# Get a list of all the file paths that ends with .txt from in
# specified directory
fileList = glob.glob("C:\\Users\\jatul\\AppData\\Local\\Temp\\*")

# Iterate over the list of filepaths & remove each file.
for filePath in fileList:
    try:
        remove(filePath)
    except:
        print("Error while deleting file : ", filePath)

# This is commit 1
# This is commit 2
# This is commit 3