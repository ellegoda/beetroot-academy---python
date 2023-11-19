f = open("my-file.txt", "w")
f.write("Hello file world!")
f.close()

f = open("my-file.txt", "r")
print(f.read())
f.close()

