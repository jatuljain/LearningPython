# mystr = "This needs to be reversed"
mystr = input("Enter the string to be reversed : reverse")
# print(mystr)

l1 = list(mystr.split(" "))
# print (l1)

l1.reverse()

# print (l1)

reversedstring = " "
reversedstring = (str(reversedstring.join(l1)))

print(reversedstring)


# # Python code to Reverse each word
# # of a Sentence individually
#
# # Function to Reverse words
# def reverseWordSentence(Sentence):
#     # Spliting the Sentence into list of words.
#     words = Sentence.split(" ")
#
#     # Reversing each word and creating
#     # a new list of words
#     # List Comprehension Technique
#     newWords = [word[::-1] for word in words]
#
#     # Joining the new list of words
#     # to for a new Sentence
#     newSentence = " ".join(newWords)
#
#     return newSentence
#
#
# # Driver's Code
# Sentence = "GeeksforGeeks is good to learn"
# # Calling the reverseWordSentence
# # Function to get the newSentence
# print(reverseWordSentence(Sentence))



#####################
## Reverse a string
#####################

def reverse_string(string):
	reverse_string = ''
	num = len(string) - 1
	for i in string:
		reverse_string += string[num]
		num-=1
	return reverse_string

print(reverse_string("Example String"))