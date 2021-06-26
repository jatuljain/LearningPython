import os

"""
This program is to search particular error lines in all the files on a given directory and subdirectories

"""

path = "D:\\Personal\\Automation\\Python\\LearningPython\\LearningPython"

files = []
# r = root, d = directories, f = files
for r, d, f in os.walk(path):
    # print("root, directory and file", r, d, f)
    for file in f:
        if ".txt" in file:
            files.append(os.path.join(r, file))  # This will create a list of File names

print("list of all text Files to be checked\n", files)
count = 0
for f in files:
    # print(f)
    with open(f) as myFile:
        for num, line in enumerate(myFile, 1):
            if "error" in line or "fail" in line:
                count += 1
                print("\n", line)
                print("{} found at line {} in file {}\n\n".format(count, num, myFile))
