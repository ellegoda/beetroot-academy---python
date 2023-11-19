index = 0
list_02 = []
list_01 = list(range(1, 101))

while index < 100:
    if (list_01[index] % 7) == 0 and (list_01[index] % 5) != 0:
        list_02.append(list_01[index])
    index += 1

print(list_02)
