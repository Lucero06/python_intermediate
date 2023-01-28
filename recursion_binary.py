# Fix the code by adding the base case for the recursion,
# then take a number from user input and call the convert() function,
# to output the result.
def convert(num):

    if (num == 0):
        return num % 2
    return (num % 2 + 10 * convert(num // 2))


decimal = input()

print(convert(int(decimal)))
