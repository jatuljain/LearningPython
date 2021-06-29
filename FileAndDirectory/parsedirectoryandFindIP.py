import os
import glob

"""
This program is to search particular error lines in all the files on
 a given directory and subdirectories

"""

# path = "D:\\Personal\\Automation\\Python\\LearningPython\\LearningPython"
path = "D:\\Personal\\Automation\\Python\\LearningPython\\LearningPython\\*.txt"

"""
    Get all file names from os.walk, Create a list of file names files 
    with .txt extension
"""
# files = []
# # r = root, d = directories, f = files
# for r, d, f in os.walk(path):
#     # print("root, directory and file", r, d, f)
#     for file in f:
#         if ".txt" in file:
#             files.append(os.path.join(r, file))  # This will create a list of File names

# print("list of all text Files to be checked\n", files)
"""
    With the list of file names in files, open each file in loop and 
    read each line and search for error or fail in that line.
"""

# Easiest way to iterate over files is glob
filewithglob = glob.glob(path)
# print(filewithglob)
count = 0
for f in filewithglob:
    # print(f)
    with open(f) as myFile:
        for num, line in enumerate(myFile, 1):
            if "error" in line or "fail" in line:
                count += 1
                print("", line)
                # print("{} found at line {} \n".format(count, num))
                print("{} found at line {} in file {}\n".format(count, num, myFile))
