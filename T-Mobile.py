"""
# Preface
The goal of this exercise is to write a small program or script, that lets the user input words (strings), which are printed back to the user in alphabetic order using **right-to-left reading order**. In other words, sorting starts at the right-most character of each word.
Pick any language you like!
# Example
##### Sample input:
cat<br/>
bunny<br/>
dog<br/>
bat
##### Sample output:
dog<br/>
bat<br/>
cat<br/>
bunny
"""

newL=[]
revL=[]
L = ["cat","bunny","dog","bat"]
print (L) 	
for word in L:
    txt = word[::-1]
    # print (txt)
    newL.append(txt)

newL.sort()
# print(newL)   
for rword in newL:
    rtxt = rword[::-1]
    # print (rtxt)
    revL.append(rtxt)
print("Sorted list by last letter: ", revL) 



# ----------------------------------------------------------------
########
# # Another way
#  
def last_letter(word):
    return word[::-1]
SL= sorted(L, key=last_letter)
print("Sorted list by last letter by using Function: ", SL) 


# ----------------------------------------------------------------
