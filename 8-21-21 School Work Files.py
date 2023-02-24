# def ReadFile():
#     file = input("Enter a filename: ")
#     num_line = 0
#     f = open(file, 'r')
#     for line in f:
#         num_line += 1
#     print("There are {} lines in the file {}.".format(num_line, file))
# ReadFile()
myFile = 'data.txt'
from_file = open(myFile, 'r')
contents = from_file.read()
from_file.close()

words = contents.split()
total_words = len(words)
total_chars = len(contents)
avg_words = float(total_chars / total_words)


print(contents)
print(total_words)
print(total_chars)
print(avg_words)