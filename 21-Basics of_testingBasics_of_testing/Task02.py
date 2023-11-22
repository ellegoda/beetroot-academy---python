# Python calculator
class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_sum(self):
        return self.a + self.b

    def get_difference(self):
        return self.a - self.b

    def get_product(self):
        return self.a * self.b

    def get_quotient(self):
        return self.a / self.b

    def get_mod(self):
        return [self.a % 2 == 0, self.b % 2 == 0]

    def get_pow(self):
        return [self.a ** 2, self.b ** 2]


if __name__ == "__main__":
    c = Calculator(15, 5)
    print(c.get_sum())
    print(c.get_difference())
    print(c.get_product())
    c = Calculator(20, 10)
    print(c.get_quotient())
    print(c.get_mod())
    print(c.get_pow())











