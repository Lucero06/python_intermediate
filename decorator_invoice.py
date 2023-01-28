# You need to add a decorator for the invoice() function,
# that will print the invoice in the following format:

# Sample Input
# 42

# Sample Output
# ***
# INVOICE #42
# ***
# END OF PAGE

# your code goes here
def decor(func):
    def wrap(n):
        print("***")
        func(n)
        print("***")
        print("END OF PAGE")
    return wrap


@decor
def invoice(num):
    print("INVOICE #" + num)


invoice(input())
