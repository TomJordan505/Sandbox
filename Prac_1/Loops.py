# count in 2's
for i in range(1, 21, 2):
    print(i, end=' ')
print('\n')

# count in 10's
for x in range(0, 110, 10):
    print(x, end=' ')
print('\n')

# count back in 1's
for y in range(20, 0, -1):
    print(y, end=' ')
print('\n')

# Print a specified number of stars
stars = int(input("How many stars? "))
for s in range(stars):
    print("*", end=' ')
print('\n')

for l in range(stars):
    print("*" * (l + 1), end=' ')
    print("\n")
