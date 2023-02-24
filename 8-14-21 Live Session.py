# define your function ONCE
def myFunction(parameter): # parameters aren't like normal "variables"
    # x= 5 don't do this with parameters
    return parameter # ends the execution of the function
    print(parameter) # this will never happen because of the return

#call my function many times
print(myFunction("Hello"))
print(myFunction("Hi Bobby"))

# Good function
#square a number
def squareThis(num):
    return num * num
    # return num**2 also works

print(squareThis(6))
x = squareThis(5)
print(x)

# Bad Function
def squareSomething(num):
    num = 5 # don't do this because it's always 5!
    return num**2
print(squareSomething(6))

#variable.method()
#myList.aListMethd()
#myString.aStringMethod()

# help(str) prints help screen
print(dir(str))
help(str.count)

def countUpper(myMessage):
    #myMessage.isupper()
    count = 0
    for charString in myMessage:
        if charString.isupper():
            count += 1
    return count
print(countUpper('Welcome to WGU'))
print(countUpper('Hello Chris'))