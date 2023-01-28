
# Sending "r" means open in read mode, which is the default.
# Sending "w" means write mode, for rewriting the contents of a file.
# Sending "a" means append mode, for adding new content to the end of the file.
# Adding "b" to a mode opens it in binary mode, which is used for non-text files
# (such as image and sound files).

# This ensures that the file is always closed, even if an error occurs.
try:
    f = open("books.txt", "w+")
    cont = f.read()
    print(cont)
finally:
    f.close()

# An alternative way of doing this is by using with statements.
# This creates a temporary variable (often called f),
# which is only accessible in the indented block of the with statement.
with open("books.txt") as f:
    print(f.read())
# The file is automatically closed at the end of the with statement,
# even if exceptions occur within it.


n = int(input())

file = open("numbers.txt", "w+")
# your code goes here
for i in range(0, n):
    file.write(str(i+1)+str("\n"))
file.close()
f = open("numbers.txt", "r")
print(f.read())
f.close()


# binary write mode
file = open("filename.txt", "wb")
file.close()

# print all of the contents of the file.
file = open("books.txt")
cont = file.read()
print(cont)
file.close()
# you can provide the number of bytes to read as an argument to the read function.
# Each ASCII character is 1 byte:
# this will read the first 5 characters of the file, then the next 7.
file = open("/usercode/files/books.txt")
print(file.read(5))
print(file.read(7))
print(file.read())
file.close()


# To retrieve each line in a file,
# you can use the readlines() method
# to return a list in which each element is a line in the file.
file = open("/usercode/files/books.txt")

for line in file.readlines():
    print(line)

file.close()

# If you do not need the list for each line,
# you can simply iterate over the file variable:
file = open("/usercode/files/books.txt")

for line in file:
    print(line)

file.close()

# This will create a new file called "newfile.txt" and write the content to it.
file = open("newfile.txt", "w")
file.write("This has been written to a file")
file.close()

file = open("/usercode/files/books.txt", "a")
# This will add a new line with a new book title to the file.
file.write("\nThe Da Vinci Code")
file.close()

# The write method returns the number of bytes written to a file, if successful.
msg = "Hello world!"
file = open("newfile.txt", "w")
amount_written = file.write(msg)
print(amount_written)
file.close()
