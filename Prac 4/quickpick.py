import random

numbers_line = 6
min_number = 1
max_number = 45

quickpicks = int(input("How many Quick picks do you want to generate? "))
while quickpicks < 1:
    quickpicks = int(input("Enter a number larger than 0? "))
for line in range(quickpicks):
    quickpick = []
    for i in range(numbers_line):
        number = random.randint(min_number, max_number)
        while number in quickpick:
            number = random.randint(min_number, max_number)
        quickpick.append(number)
    quickpick.sort()
    print(" ".join(" {:2}".format(number) for number in quickpick))