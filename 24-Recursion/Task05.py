def sum_of_digits(digit_string: str) -> int:
    if digit_string == "":
        return 0
    else:
        if digit_string[0].isdigit():
            return sum_of_digits(digit_string[1:]) + int(digit_string[0])
        else:
            raise ValueError("input string must be digit string")


print(sum_of_digits('26') == 8)
print(sum_of_digits('1234') == 10)
print(sum_of_digits('test'))
