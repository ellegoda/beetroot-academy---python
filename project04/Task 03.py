import string
import random

word = input("Enter your string here : ")

for i in range(5):
    random_word = ''.join(random.choices(word, k=len(word)))
    print("The generated random string : ", random_word)
