import random

index = 0
list_1 = random.sample(range(1, 11), 10)
list_2 = random.sample(range(1, 11), 10)
list_3 = []

while index < 10:
    if list_1[index] in list_2:
        list_3.append(list_1[index])
    index += 1

print(list_1)
print(list_2)
print(list_3)
