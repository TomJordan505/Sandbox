from Prac_8.taxi import Taxi

def main():
    test = Taxi('prius 1', 100, 1.23)
    test.drive(40)
    print(test)
    test.start_fare()
    test.drive(100)
    print(test)

main()