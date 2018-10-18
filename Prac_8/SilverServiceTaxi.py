from Prac_8.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Car that includes fare costs."""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel, price_per_km=5)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        #return "{} plus flagfall cost of {:.2f}/km".format(super().__str__(),
         #                                                 4.5)
        return "{} plus flagfall cost of {:.2f}/km".format(super().__str__(),
                                                           self.flagfall)

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + self.flagfall
