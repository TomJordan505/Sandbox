name = input("What is your name? ")
out_file = open("Name", 'w')
print("Your name is {}".format(name), file=out_file)
out_file.close()