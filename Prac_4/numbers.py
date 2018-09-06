numbers = []
for i in range(5):
    number = int(input("Enter an integer for number {}: ".format(i+1)))
    numbers.append(number)

print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[-1]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
print("the average of numbers is {}".format(sum(numbers)/len(numbers)))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
             'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole',
             'InterpreterInterface', 'StartServer', 'bob']

login = input("What is you username? ")
while login not in usernames:
    login = input("Invalid username. Try again...")
print("Access granted")