import random
index = 0
large_number = 0
numbers = random.sample(range(1, 100), 10)

while index < 10:
    if large_number < numbers[index]:
        large_number = numbers[index]

    index += 1

print("Numbers", numbers)
print("Large Number", large_number)


