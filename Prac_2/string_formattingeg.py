name = "Gibson L-5 CES"
year = 1922
cost = 16035.40

# The 'old' manual way to format text with string concatenation:
print("My guitar: " + name + ", first made in " + str(year))

# A better way - using str.format():
print("My guitar: {}, first made in {}".format(name, year))
print("My guitar: {0}, first made in {1}".format(name, year))
print("My {0} was first made in {1} (that's right, {1}!)".format(name, year))

# Formatting currency (grouping with comma, 2 decimal places):
print("My {} would cost ${:,.2f}".format(name, cost))

# Aligning columns:
numbers = [1, 19, 123, 456, -25]
for i in range(len(numbers)):
    print("Number {0} is {1:>5}".format(i + 1, numbers[i]))

# Another (nicer) version of the above loop using the enumerate function
for i, number in enumerate(numbers):
    print("Number {0} is {1:>5}".format(i + 1, number))

print("\n")
# first task
tnumbers = [0, 50, 100]
for i in range(len(tnumbers)):
    print("Number {0} is {1:>5}".format(i + 1, tnumbers[i]))

for i, num in enumerate(tnumbers):
    print("Number {0} is {1:>5}".format(i + 1, num))

# print(random.randint(5, 20)) = 6
# print(random.randrange(3, 10, 2)) = 3
# print(random.uniform(2.5, 5.5)) = 4.983999311758126
