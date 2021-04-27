import os
'''
This program is to search particular error lines in all the files on a given directory and subdirectories

'''

path = 'E:\\Python\\'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.txt' in file:
            files.append(os.path.join(r, file)) ## Joining file name with root and making a list

count = 0
for f in files:
    # print(f)
    with open(f) as myFile:
        for num, line in enumerate(myFile, 1):
            if "error" in line or "fail" in line:
                count += 1
                print(line)
                print('{} found at line {} in file {}'.format(count, num, myFile) )


