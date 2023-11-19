# Simple calculator
def make_operation(operator, *numbers):
    calculated = numbers[0]
    for number in numbers[1:]:
        if operator == "+":
            calculated += number
        elif operator == "-":
            calculated -= number
        elif operator == "*":
            calculated *= number
    print(calculated)


make_operation('+', 7, 7, 2)  #should return 16
make_operation('-', 5, 5, -10, -20)  #should return 30
make_operation('*', 7, 6)  #should return 42
make_operation("+", 1,9,8,3,1,0,1,0)
