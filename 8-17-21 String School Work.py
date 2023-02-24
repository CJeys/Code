# def fourthChar(myString):
#     newString = ""
#     ch = 1
#     for i in range(0, len(myString)):
#         if ch == 4:
#             newString += myString[i]
#             ch = 1
#         ch += 1
#     return newString
# print(fourthChar("abcdefg"))
# print(fourthChar("abc def rgj"))

# def lastCharInStrings(strList):
#     newStr = ""
#     for i in strList:
#         newStr += i[len(i) - 1]
#     return newStr
#
# strList = ["abc", "def", "rgi"]
# print(lastCharInStrings(strList))

# String slicing
# str[start : end : stride/step]
# longString = "Here at WGU, we believe that talent is universal-even if opportunity isn't.  Higher education is the \
#     best way yASDASD sdasdaSAsd ASDAsdaSD asdASDasd ASDAf SDFSDFASdaSDAs fAFSDFsdfASF asdA SFdsfASFA SFsdfASDFASAFDASD \
#     ssfdsdfasdfasdfasdfasd asdfasdf asdfasdfasdf asdfas dfas gerrgewt gerg qerg qer gqwe wfw werw erwqer wer we."
# shortString = "WGU exists to change lives"
#
# def longSentences(sentence):
#     if (len(sentence) > 45):
#         return(sentence[:40] + "...")
#     else:
#         return(sentence)
# print(longSentences(longString))
# print(longSentences(shortString))

# string = input("Enter a string: ")
# def everyTwoChars(myString):
#         return myString[::2]
# print(everyTwoChars(string))

# string = input("Enter a string: ")
# def isPalindrome(myString):
#     reverseString = string[::-1]
#     if reverseString == myString:
#         return True
#     return False
# if isPalindrome(string):
#     print("{}, is a palindrome".format(string))
# else:
#     print("{}, is not a palindrome".format(string))

# list = ["banana", "orange", "strawberries"]
# print("The list is:", list)
# print("The list is: %s" % list)
# print("The list is: " + str(list))
# print("The list is: {}".format(list))
#
# dictionary = {
#     'a': 1,
#     'b': 2
# }
# print("The dictionary is:", dictionary)
# print("The dictionary is: %s" % dictionary)
# print("The dictionary is: " + str(dictionary))
# print("The dictionary is: {}".format(dictionary))
#
# tup = ("element", "another")
# print("The tuple is:", tup)
# print("The tuple is: %s" % (tup,))
# print("The tuple is: " + str(tup))
# print("The tuple is: {}".format(tup))
#
# string = "Hello There"
# print("The string is:", string)
# print("The string is: %s" % string)
# print("The string is: " + str(string))
# print("The string is: {}".format(string))

# floatPrint = float(input("Enter the floating point value: "))
# print("Formatting the number %f to 2 decimal places is %.2f" % (floatPrint, floatPrint))
# print("Formatting the number {} to 2 decimal places is {:.2f}".format(floatPrint, floatPrint))
# print("Formatting the number {} to 2 decimal places is {}".format(floatPrint, round(floatPrint, 2)))

# def replaceString(myString):
#     if myString.find('858') > 0:
#         newString = myString.replace('858', '760')
#     print(newString)
# string = "My area code in San Diego is 858."
# replaceString(string)

def acronym(string):
    words = string.split()
    letters =[]
    for word in words:
        letters.append(word[0])
    return ''.join(letters)
    print(words)
phrase = "BY THE WAY"
print(acronym(phrase))