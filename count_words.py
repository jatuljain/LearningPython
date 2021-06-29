"""
Count the word in a line
"""


def count_words(text):
    return str(len(text.split(" ")))  # + " words in the analyzed text"


"""[summary]
Count the word in a file calling a Count_word in a line function
"""


def count_from_file(file_location):
    file = open(file_location, "r")
    text = str(file.read())
    return count_words(text)


filename = "FiletoCheckAmend.txt"

# print(count_words("This is a sentence with 7 words"))
print("{} words in file {}".format(count_from_file(filename), filename))
