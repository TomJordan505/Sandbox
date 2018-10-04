from Prac_8.SilverServiceTaxi import SilverServiceTaxi

def main():
    test = SilverServiceTaxi('fancy', 100, 7.24)
    test.drive(40)
    print(test)
    test.start_fare()
    test.drive(100)
    print(test)

main()