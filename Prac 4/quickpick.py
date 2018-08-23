import random

NUMBERS_PER_QUICKPICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

quickpicks = int(input("How many Quick picks do you want to generate? "))
while quickpicks < 1:
    quickpicks = int(input("Enter a number larger than 0? "))
for line in range(quickpicks):
    quickpick = []
    for i in range(NUMBERS_PER_QUICKPICK):
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        while number in quickpick:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
        quickpick.append(number)
    quickpick.sort()
    print(" ".join(" {:2}".format(number) for number in quickpick))