import unittest
from Task02 import Calculator


class Test_Calculator(unittest.TestCase):
    def test_sum(self):
        calculator = Calculator(15, 5)
        self.assertNotEqual(calculator.get_sum(), 12,"The sum value total is wrong")

    def test_difference(self):
        calculator = Calculator(15, 5)
        self.assertNotEqual(calculator.get_difference(), 5,"The differance value total is wrong")

    def test_product(self):
        calculator = Calculator(15, 5)
        self.assertNotEqual(calculator.get_product(), 25,"The Total product value is wrong")

    def test_quotient(self):
        calculator = Calculator(20, 10)
        self.assertEqual(calculator.get_quotient(),2.0, "The total divided value is correct")

    def test_mod(self):
        calculator = Calculator(20, 10)
        self.assertEqual(calculator.get_mod(),[True, True], "The both a and b modulator values are true")

    def test_pow(self):
        calculator = Calculator(20, 10)
        self.assertEqual(calculator.get_pow(), [400,100], "The both power values are correct")
