email_dict = {
    "john.doe@tech.com":"John Doe",
    "john.hancock@tech.com":"John Hancock",
    "jane.doe@tech.com":"Jane Doe",
}
email_dict_v2 = {
    "john.doe@tech.com":[2012, 60000.0],
    "john.hancock@tech.com":[2020, 45000.0],
    "jane.doe@tech.com":[2018, 55000.0],
}
print(email_dict["john.doe@tech.com"])
print(email_dict_v2["john.doe@tech.com"])
print(email_dict_v2["john.doe@tech.com"][1])

# The <in> and <not in> Operators check if a key exists in a dictionary
#General format
# if key in dictionary_name:
#   Do something
#OR
# if key not in dictionary_name:
#   Do something
# <in> and <not in> operators are boolean value of True or False

# if "john.doe@tech.com" in email_dict_v2:
#     print("Key found!")
#     print(email_dict_v2["john.doe@tech.com"])
# else:
#     print("Key not found.")
#
# if "jane.doe@tech.com" not in email_dict_v2:
#     print("True, key is not found")
#     print(email_dict_v2["john.doe@tech.com"])
# else:
#     print("Key found!")

# Adding elements to a dictionary
# dictionary_name[key]=value

email_dict_v2["chris.jeys@tech.com"] = [2020, 150000]
print(email_dict_v2)
email_dict["jane.doe@tech.com"] = "Jane A. Doe"
print(email_dict)

# Deleting elements
# del dictionary_name[key]
#
#You can use <in> operator to check if key exists first before deleting
#if key in dictionary_name:
#   del dictionary_name[key]

if "john.doe@tech.com" in email_dict_v2:
    del email_dict_v2["john.doe@tech.com"]
else:
    print("Key not found.")
print(email_dict_v2)

# The len() function
# len(dictionary_name)

print("There are", len(email_dict_v2), "elements in the dictionary.")