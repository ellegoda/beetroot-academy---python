from fractions import Fraction as PyFraction


class Fraction:
    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.fraction = PyFraction(numerator, denominator)

    def __add__(self, other):
        result = self.fraction + other.fraction
        return Fraction(result.numerator, result.denominator)

    def __sub__(self, other):
        result = self.fraction - other.fraction
        return Fraction(result.numerator, result.denominator)

    def __mul__(self, other):
        result = self.fraction * other.fraction
        return Fraction(result.numerator, result.denominator)

    def __truediv__(self, other):
        if other.fraction == 0:
            raise ValueError("Cannot divided by zero")
        result = self.fraction / other.fraction
        return Fraction(result.numerator, result.denominator)

    def __eq__(self, other):
        return self.fraction == other.fraction

    def __repr__(self):
        return f"Fraction({self.fraction.numerator}/{self.fraction.denominator})"

    x = PyFraction(1, 2)
    y = PyFraction(1, 4)

    result = x + y
    print(result)
    print(result == PyFraction(3, 4))
