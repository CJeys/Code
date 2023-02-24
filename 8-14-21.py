mystring = "My favorite book is Dune.  My favorite movie series is James Bond"
myList = ["Paul Atreides", "James Bond", "Oddjob"]
myTuple = ("Harkonnen", "Spacing Guild", "Bene Gesserit")
myDictionary = {"Leto": "Duke", "Paul": "Ducal heir", "Jessica": "Concubine", "Duncan": "Future Ghola"}

for list in myList:
    print((myList), "Which book and movie series is your favorite?")

for letter in mystring:
    print(letter)

for house in myTuple:
    print(house)

# enumerate()
for index, item in enumerate(myList):
    print(item + " is a fictional character.")

for howManyTimes in range(0, 5):
    print("Hello " + item)

for key in myDictionary:
    print(key, "is a", myDictionary[key])
# These two do the same thing
for key, value in myDictionary.items():
    print("{} is a {}".format(key, value))

