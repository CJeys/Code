myDay = "Friday"
if myDay == "Monday":
    print("Today is not a good day.")
elif myDay == "Tuesday" or myDay == "Wednesday" or myDay == "Thursday":
    print("You are getting close to Friday")
elif myDay == "Friday":
    print("Happy Friday!!!")
elif myDay == "Saturday" or "Sunday":
    print("Enjoy your weekend!!!")
else:
    print("I don't know what that means.")

theTemp = 70
if theTemp <= 32:
    print("It is freezing outside!")
elif theTemp <= 69:
    print("It's getting warmer but it's still brisk outside.")
elif theTemp <= 90:
    print("It's nice outside.")
else:
    theTemp <= 105
    print("It's way too hot outside!!!")
print("Have a great day!")


def cookieFunction(taste):
    cookie = None
    if taste == "peanut butter":
        cookie = "Peanut Butter Patties"
    elif taste == "mint":
        cookie = "Thin Mints"
    elif taste == "caramel":
        then = "Caramel Delites"
    elif taste == "plain":
        cookie = "Shortbread"
    if cookie:
        return "I'll place your order for {}!".format(cookie)
    else:
        return "You don't want any cookies?"
print(cookieFunction("sfadfasdf"))

colors = ["black", "blue", "green", "red"]
for color in colors:
    print("These is a color " + color)
print("Have a great colorful day!")


list = ['beer', 'water', 'pop', 'tea']
num = 1
list.sort()
for drink in list:
    print(str(num) + ". ", drink)
    num += 1

def sum_list(input_list):
    sum = 0
    for sums in input_list:
        sum = sum + sums
    return sum
print(sum_list([1, 2, 3, 4]))

# While Loop - always keep a statement which will make a False statement, otherwise will loop forever.
#grades = gradeslist() # grades = []

grades = [55, 75, 69, 74, 100, 90, 0, 95, 85, 70]
passingGrades = list()
while sum(grades) > 0:
    grade = grades.pop()
    if grade >= 75:
        passingGrades.append(grade)
print(passingGrades)





