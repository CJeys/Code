numbers = [1, 2, 3, 4, 5, "Chris", "Joe Bob"]

for items in numbers:
    print("This person is", items*2)

run = True
current = 1

while run:
    if current == 5:
        run = False
    else:
        print(current)
        current += 1
