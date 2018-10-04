from random import randint

from Prac_8.car import Car


class Unreliablecar(Car):
    """Specialised version of a Car that includes fare costs."""

    def __init__(self, name, fuel, reliability):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""

        test = randint(1, 100)
        if test >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
