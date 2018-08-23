"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    # a while loop will eliminate any chance of zero div error

    while denominator == 0:
        denominator = int(input("Enter a denominator that is not zero: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

print("Finished.")

# a value error will occur when the input is not an integer or contains a letter or symbol, eg 1.5 or h
# a zero div error will occur when a zero is given as the denominator
