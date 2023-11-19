class Mathematician:

    @staticmethod
    def square_nums(nums: list[int]):
        return list(map(lambda num: num**2, nums))

    @staticmethod
    def remove_positives(nums: list[int]):
        return list(filter(lambda num: num < 0, nums))

    @staticmethod
    def filter_leaps(years: list[int]):
        return list(filter(lambda year: (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0), years))


m = Mathematician()

numbers = [2, 4, 6, 8, 10]
squared_nums = m.square_nums(numbers)
print("Squared Numbers:", squared_nums)

num_with_positive = [26, -11, -8, 13, -90]
no_positives = m.remove_positives(num_with_positive)
print("Without positives:", no_positives)

year = [2001, 1884, 1995, 2003, 2020]
leap_year = m.filter_leaps(year)
print("Leap Years are:",leap_year)
