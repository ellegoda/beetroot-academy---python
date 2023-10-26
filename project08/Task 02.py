def numbers(a, b):
    c = (a ** 2) / b
    return c

try:
    a = int(input("Enter the first number : "))
    b = int(input("Enter the second number : "))

    print(numbers(a, b))
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid Inputs")

