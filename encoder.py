file = open("books.txt", "r")
for line in file.readlines():
    words = line.split()
    encoded = ""
    for word in words:
        encoded += word[0]
    print(encoded)

file.close()
