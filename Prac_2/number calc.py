in_file = open("numbers", "r")
total = 0
for i in in_file:
    number = int(i)
    total += number


#number1 = int(in_file.readline())
#number2 = int(in_file.readline())
#total = number1 + number2
print(total)
in_file.close()