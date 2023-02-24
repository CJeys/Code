import math as m
print(m.sqrt(9))

from random import choice as c
myList = ['apple', 'banana', 'orange']
print(c(myList))

help(m.floor)

# help(set)
# help(dict)
import datetime as dt
def currentDate():
    print("The current date is {}-{}-{}.".format(dt.date.today().month,dt.date.today().day,dt.date.today().year))
print(currentDate())

import os
def currentEnvironment():
    return("My operating system is " +str(os.name))
print(currentEnvironment())