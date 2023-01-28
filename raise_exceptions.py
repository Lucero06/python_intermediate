# You need to specify the type of the exception raised.

tweet = input()

try:
    # your code goes here
    if (len(tweet) > 42):
        raise ValueError
except ValueError:
    print("Error")
else:
    print("Posted")

# Any name that has less than 4 characters is invalid.
# Complete the code to take the name as input,
# and raise an exception if the name is invalid, outputting "Invalid Name".
# Output "Account Created" if the name is valid.
try:
    name = input()
    # your code goes here
    if (len(name) < 4):
        raise ValueError
    print("Account Created")
except:
    print("Invalid Name")


num = 102
if num > 100:
    raise ValueError

try:
    print(1 / 0)
except ZeroDivisionError:
    raise ValueError