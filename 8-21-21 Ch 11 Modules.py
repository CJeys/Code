# import datetime as dt
#
# today = dt.datetime.today()
# print("Todays date is {}/{}/{}.".format(today.month,today.day,today.year))
#
# help(dt.datetime)
# print(dir(dt))

# from datetime import date
#
# def daysWeeksBetween():
#     date_input1 = input("Enter the 1st date in yyyy-mm-dd format: ")
#     year1, month1, day1 = (map(int, date_input1.split(('-'))))
#     date1 = date(year1, month1, day1)
#
#     date_input2 = input("Enter the 2nd date in yyyy-mm-dd format: ")
#     year2, month2, day2 = (map(int, date_input2.split(('-'))))
#     date2 = date(year2, month2, day2)
#
#     d = (date2 - date1).days
#     w = d // 7
#     print("Days between {}/{}/{} - {}/{}/{} is {} days.".format(date1.month,date1.day,date1.year,date2.month,date2.day,date2.year,d))
#     print("Days between {}/{}/{} - {}/{}/{} is {} weeks.".format(date1.month, date1.day, date1.year, date2.month,
#                                                                 date2.day, date2.year, w))
#
#
# daysWeeksBetween()

# import random
# min = 1
# max = 6
#
#
# roll_again = "yes"
#
# while roll_again == "yes" or roll_again == "y":
#     print("Rolling the dice...")
#     print("The values are ...")
#     print(random.randint(min, max))
#     print(random.randint(min, max))
#
#     roll_again = input("Roll again? ")
# import random
#
# chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
# number = int(input("Number of passwords? "))
# length = int(input("Password length? "))
#
# for p in range(number):
#     password = ""
#     for c in range(length):
#         password += random.choice(chars)
#     print(password)





