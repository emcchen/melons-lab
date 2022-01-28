import random
import datetime

class TooManyMelonsError(ValueError):
    """ Error if ordering too many melons """
    def __init__(self):
        super().__init__("No more than 100 melons!")


class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""
    def __init__(self, species, qty, order_type, tax):

        if self.qty > 100:
            raise TooManyMelonsError

        self.species = species
        self.qty = qty
        self.order_type = order_type
        self.shipped = False
        self.tax = tax

    

    def get_base_price(self):
        """ Splurge pricing and rush hour fee"""

        #splurge price
        base_price = random.randrange(5, 10)

        #rush hr fee (M-F 8-11)
        time = datetime.datetime.now()
        if time.hour > 8 and time.hour < 11 and time.weekday() < 5:
            base_price += 4

        return base_price

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()

        if self.species == "Christmas melons":
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price
        if self.order_type == "international" and self.qty < 10:
            total += 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder:
    """A melon order within the USA."""

    def __init__(self, species, qty):
        super().__init__(species, qty,"domestic", 0.08)

class InternationalMelonOrder:
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty, "international", 0.17)
        self.country_code = country_code


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder:
    """ Government purchase """
    def __init__(self, species, qty, tax):
        super().__init__(species, qty, "government", 0)
        self.passed_inspection = False

    def mark_inspection(self, passed):
        """ Records if a melon order passes inspection"""
        self.passed_inspection = True
