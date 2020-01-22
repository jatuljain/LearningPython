import os

path = 'E:\\Python\\'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.txt' in file:
            files.append(os.path.join(r, file))

totallinecount = 0
for f in files:
    # print(f)
    count = len(open(f).readlines())
    print("file number count is in file %s is %d" % (f, count))
    totallinecount = totallinecount + count

print("total file number count is ", totallinecount)

# def countfileline(filepath)
#     count = len(open(filepath).readlines())
#     return count
