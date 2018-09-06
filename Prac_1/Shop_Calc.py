total = 0
items = int(input("number of items? "))

while items < 0:
    print("Invalid input")
    items = int(input("Please input a valid numebr of items..."))

for x in range(items):
    price = float(input("What is the price of item {}?  $".format(x + 1)))
    total += price
if total >= 100:
    total = 0.9 * total
print("The total price of your items is $", total, sep="")
