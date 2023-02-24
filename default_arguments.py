# Script made on 6/26/21
def print_something(name, age) -> object:
    print('My name is', name, "and my age is", age)


print_something('Chris', 38)


# Script made on 6/26/21
def print_something2(name="Someone", age="Unknown") -> object:
    print('My name is', name, "and my age is", age)


print_something2()


# Script made on 6/26/21 - Keyword arguments
def print_something3(name="Someone", age="Unknown") -> object:
    print('My name is', name, "and my age is", age)


print_something3(age=38, name='JoeBob')
