def fuelCal(miles, gallons):
    mpg = miles / gallons
    return mpg


print(fuelCal(350, 15))

myname = "Christopher"
print(myname[7])
print(len(myname))

list = [1, 6, 9, 3, 4]
product = 1
for num in list:
    product *= num
print(product)

OGlist = [1, 6, 9, 3, 4]
print("The original list is: " + str(OGlist))

result = []
for elements in OGlist:
    result.append(elements * 3)
print("The list tripled is: " + str(result)[1:-1])
print(result[3])
result.remove(12)
print(result)
result.append(34)
print(result)

myname = ["Chris", "John", "Jeys"]
print(', '.join(myname))

# Tuples
tup = ("this", "is", "a", "tuple")
newtuple = ()

username = input("Enter your Last Name: ")
tuplesize = len(tup)

newtuple = newtuple + (tup[0], username, tup[tuplesize - 1])
print(newtuple)

# Sets
mylist = [1, 3, 4, 4, 5, 3, 7]
print("Original List is: " + str(mylist))

mySet = set(mylist)
# mylist = list(mySet)
print("My new list is: " + str(mylist))

#
animalset = set()
animalset.add('dog')
animalset.add('cat')
animalset.add('eagle')
animalset.add('python')

animalset.remove('eagle')
print(animalset)

#myAnimalList = list(animalset)
#myAnimalList.pop(1)
#print(myAnimalList)

# Dictionary

DuneCharacters = {
    "Leto": "Duke",
    "Paul": "Ducal heir",
    "Jessica": "Concubine",
    "Duncan": "Future Ghola",
}

for chars, position in DuneCharacters.items():
    print('{} : {}'.format(chars, position))

DuneCharacters['Gurney'] = 'Swordmaster'
print(DuneCharacters)

print('{} : {}'.format(chars, position))
