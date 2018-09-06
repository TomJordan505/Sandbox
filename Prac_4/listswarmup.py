numbers = [3, 1, 4, 1, 5, 9, 2]
print(numbers)
#3, 2, 1, [3,1,4,1,5,9],1, true, false, false, [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
numbers[0] = "ten"
print(numbers)
newnumbers = numbers[0:len(numbers)-2]
print(newnumbers)
9 in numbers
