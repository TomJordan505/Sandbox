from Prac_6.guitar import Guitar

def main():
    guitars = []
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = int(input("Cost: "))
        print("{} ({})  :  ${} added".format(name, year, cost))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        name = input("Name: ")

    for i, guitar in enumerate(guitars):
        if guitar.is_vintage():
            print("Guitar {}: {} ({}), worth ${} (Vintage)".format(i, guitar.name, guitar.year, guitar.cost))
        else:
            print("Guitar {}: {} ({}), worth ${}".format(i, guitar.name, guitar.year, guitar.cost))


main()