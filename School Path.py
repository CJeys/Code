#Lesson 3 Example 1 from WK1 Bootcamp
mystring = input("Enter string here: ")
if len(mystring) < 2:
    print("You need a bigger string.")
else:
 print(mystring[:2] + mystring[-2:])

#Example 2 Basic Math
print("Select an operation - \n \
      1. Add \n \
      2. Subtract\n \
      3. Exit\n \
")
select = int(input("Select 1, 2, or 3: "))
number1 = int(input("Please pick a number, any number: "))
number2 = int(input("Please pick another number: "))
if select == 3:
    print("Goodbye...")
    exit()

elif select == 1:
    sum = number1 + number2
    print(sum)
elif select == 2:
    difference = number1 - number2
    print(difference)
else:
    print("You made an invalid selection.")

#Example 3
seconds = int(input("Enter a number of seconds: "))
hours = seconds // 3600
minute_remainder = seconds % 3600
minutes = minute_remainder // 60
seconds = minute_remainder % 60

print("Here is the time in hours, minutes, and seconds: ")
print("Hours: ", hours)
print("Minutes: ", minutes)
print("Seconds: ", seconds)

#Example 4
number3 = float(input("Enter a number to round: "))
print("Original value: ", number3)
print("Rounded Value: ", round(number3, 2))

#Example 5
import math
print("Floor: ", math.floor(3.1))
print("Ceiling: ", math.ceil(3.1))
print("Round: ", round(3.5))
print("Round: ", round(2.5))