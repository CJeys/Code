# While Loop - always keep a statement which will make a False statement, otherwise will loop forever.
# grades = gradeslist() # grades = []

grades = [55, 75, 69, 74, 100, 90, 0, 95, 85, 70]
passingGrades = list()
while len(grades) > 0:
    grade = grades.pop()
    if grade >= 75:
        passingGrades.append(grade)
        passingGrades.sort()
print(passingGrades)


def even_nums(check_even):
    even_list = list()
    while check_even >= 0:
        if check_even % 2 == 0:
            even_list.append(check_even)
        check_even -= 1
    even_list.sort()
    return even_list


print(even_nums(42))

menu = ["Hamburger", "Cheeseburger", "Chicken", "Pepsi", "Coke", "water"]
print("Menu:\n", "\n".join(menu))

print("Food: " + ", ".join(menu[:3]))
# print("Drink: " + ", ".join(menu[:-3]))
#
# meal = input("What would you like to eat? ")
# if meal in menu:
#    print("The customer wants a {}".format(meal))
# else:
#     print("We do not have this item.")
# drink = input("What would you like to drink? ")
# if meal in menu:
#     print("The customer would like a {}".format(menu))
# else:
#     print("We do not have this item.")
# print("You want a " + meal, "with a " + drink, "correct?")

# distance = int(input("How far do you want to travel? "))
# if distance < 3:
#     mode_of_transport = "walking"
# elif distance < 300:
#     mode_of_transport = "driving"
# else:
#     mode_of_transport = "flying"
# print("I suggest {} to your destination.".format(mode_of_transport))

# films = {
#     "Dune": [17, 3],
#     "The Hobbit": [13, 1],
#     "Lord of the Rings": [13, 3],
#     "TekWar": [13, 10],
#     "The Transporter": [13, 0],
# }
#
# choice = input("Which movie do you want to see?" ).strip().title()
# if choice in films:
#     age = int(input("How old are you? ").strip())
#     if age >= films[choice][0]:
#         num_seats_bought = films[choice][1]
#         num_seats = int(input("How many tickets do you want?" ))
#         if num_seats < num_seats_bought:
#             print("Enjoy the film " + choice + "!")
#             films[choice][1] = films[choice][1] - num_seats
#         else:
#             print("Sorry, we are sold out.")
#     else:
#         print("You are too young too watch this movie!  You are better off watching The Hobbit.")
# else:
#     print("This film does not exist." )

