import sys

list_eg = [1, 2, 3, "a", "b", "c", True, 3.14159]
tuple_eg = (1, 2, 3, "a", "b", "c", True, 3.14159)

print(dir(sys))
print(sys.getsizeof(list_eg))
print(sys.getsizeof(tuple_eg))

import timeit

list_test = timeit.timeit(stmt="[1,2,3,4,5]", number=10000000)
tuple_test = timeit.timeit(stmt="(1,2,3,4,5)", number=10000000)

print("The List time is ", list_test)
print("The tuple time is ", tuple_test)

empty_tuple = ()
empty_list = []
test1 = ("a",)
test2 = ("a", "b")
test3 = ("a", "b", "c")

print(empty_tuple)
print(test1)
print(test2)
print(test3)

test4 = 1,
test5 = 1, 2
test6 = 1, 2, 3

print(test4, type(test4))
print(test5, type(test5))
print(test6, type(test6))

# (age, country, knows_python)
survey = (27, "Japan", True)

age = survey[0]
country = survey[1]
knows_python = survey[2]
print(age)
print(country)
print(knows_python)

survey2 = (38, "Canada", False)
age, country, knows_python = survey2
print(age)
print(country)
print(knows_python)

