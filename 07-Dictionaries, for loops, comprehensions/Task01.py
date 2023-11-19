
word_dict = {}

words = input("Enter your sentence here: ")
for word in words.split():
    if word in word_dict:
        v = int(word_dict.get(word)) + 1
        word_dict[word] = v
    else:
        word_dict[word] = 1

print(word_dict)




