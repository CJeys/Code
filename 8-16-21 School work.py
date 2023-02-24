# films = {
#      "Dune": [17, 3],
#      "The Hobbit": [13, 1],
#      "Lord of the Rings": [13, 3],
#      "TekWar": [13, 10],
#      "The Transporter": [13, 0],
#  }
# while True:
#  choice = input("Which movie do you want to see?" ).strip().title()
#  if choice in films:
#      age = int(input("How old are you? ").strip())
#      if age >= films[choice][0]:
#          num_seats_bought = films[choice][1]
#          num_seats = int(input("How many tickets do you want?" ))
#          if num_seats < num_seats_bought:
#              print("Enjoy the film " + choice + "!")
#              films[choice][1] = films[choice][1] - num_seats
#          else:
#              print("Sorry, we are sold out.")
#              break
#      else:
#          print("You are too young too watch this movie!  You are better off watching The Hobbit.")
#  else:
#      print("This film does not exist." )

#Loops

# year = int(input("Enter your year: "))
# while year != 0:
#     if (year % 4) == 0 or (year % 100) == 0 and (year % 400) == 0:
#         print("{} is a leap year.".format(year))
#     else:
#         print("{} is not a leap year.".format(year))
#     break
# else:
#     print("{} is a leap year.".format(year))

# Nested loop
# students = {
#     "male": ["Tom", "Charlie", "Harry", "Frank"],
#     "female": ["Sarah", "Huda", "Samanatha", "Emily", "Elizabeth"]
# }
# for key in students.keys():
#     for name in students[key]:
#         if 'a' in name:
#             print(name)

# list = ["John", "Sheila", "Roger", "Manuel", "Shelly"]
# for i in list:
#     if i == "Roger":
#         print("Searched for {} in the list above.".format(i))
#         break
#     print("Current name " + i)

employeeDatabase ={
    "Rob Parker" : 65000,
    "Alexandra Hamilton" : 40000,
    "Chris Hemsworth" : 150000,
    "Julia Hernandez" : 35000,
    "Sonny Weathers" : 25000,
}

for employee, value in employeeDatabase.items():
    newSalary = employeeDatabase[employee] * 1.05
    if value > 50000:
        continue
        print(value)
    print("{}, your current salary is {}.  You received a 5% raise. This makes your salary {}".format(employee, employeeDatabase[employee], newSalary))


