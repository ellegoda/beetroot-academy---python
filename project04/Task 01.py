import random

count = 0
while True:

    count += 1
    generate_no = random.randint(1, 10)
    guess_no = int(input("Enter your guess no : "))
    print("This is the random generate number ",generate_no)
    break
