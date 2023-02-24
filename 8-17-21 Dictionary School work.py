# Creating an empty dictionary
# dictionary_name={}
# Adding elements to a dictionary
# dictionary_name[key]=value

name_dict = {}
name_dict["John Doe"] = 'Foreman'
name_dict["Jane Doe"] = 'Secretary'
name_dict["Billy Bob"] = 'Farmer'

print(name_dict["John Doe"])

# Iteration (repeating)
# You can use a for Loop to iterate over all keys in a dictionary
# for key in dictionary_name:
#   Do something

for key in name_dict:
    print(key, name_dict[key])

name_dict.clear()  # clears the dictionary
print(name_dict)

name_dict["John Doe"] = 'Foreman'
name_dict["Jane Doe"] = 'Secretary'
name_dict["Billy Bob"] = 'Farmer'

value = name_dict.get("John Doe", 'Key not found') # Key not found is the default message we want in case there isn't a key
print(value)

for key, value in name_dict.items(): # Returns all keys in a dictionary AND their associated values
    print(key, value)

value1 = name_dict.pop("Billy Bob", "Key not found") # Returns value associated with key and removes the key, if the key isn't found, the default message is printed.
print(value1)
print(name_dict)

print(name_dict.keys()) # Returns all keys
print(name_dict.values()) # Returns all values
for value in name_dict.values(): # Notice the slight difference in display
    print(value)
