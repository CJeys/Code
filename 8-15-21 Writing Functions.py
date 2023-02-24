# def [name of function]([parameter]):
#   [body]
# [function call][(arguments)]
#

def myFunction(greeting):
    print(greeting)
myFunction("Hi Bob")
myFunction("Hi Crystal")

def myFunction2(greeting, name):
    print(greeting + ", " + name + "!")
myFunction2("Hola", "Chris")

def myFunction3(subtotal):
    check =subtotal + (subtotal * .09)
    return check
print(myFunction3(50))


