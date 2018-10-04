from Prac_8.UnreliableCar import Unreliablecar

def main():
    test = Unreliablecar('t1', 100, 95)
    test2 = Unreliablecar('t2', 100, 15)
    test.drive(40)
    print(test)
    test.drive(40)
    print(test)
    test.drive(40)
    print(test)
    test.drive(40)
    print(test)
    test2.drive(50)
    print(test2)
    test2.drive(50)
    print(test2)
    test2.drive(50)
    print(test2)
    test2.drive(50)
    print(test2)

main()