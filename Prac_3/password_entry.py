"""Thomas Jordan"""

PASSWORD_LENGTH = 6


def main():
    password = get_password()
    print_stars(password)


def get_password():
    password = input("Please enter a {} character password: ".format(PASSWORD_LENGTH))

    while len(password) < PASSWORD_LENGTH:
        password = input("Please enter a {} character password: ".format(PASSWORD_LENGTH))
    return password


def print_stars(sequence):
    print("*" * len(sequence))


main()
