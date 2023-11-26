
def reverse(string):
    string = [string[i] for i in range(len(string) - 1, -1, -1)]
    return "".join(string)


s = "Hello Python"
print("The original string is : ", s)
print("The reversed string using reversed is : ", reverse(s))
