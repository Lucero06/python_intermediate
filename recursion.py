def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)


print(factorial(5))

# Furthermore, 1! = 1.
# This is known as the base case,
# as it can be calculated without performing any more factorials.

# The base case acts as the exit condition of the recursion.
# Not adding a base case results in infinite function calls, crashing the program.


# Recursion can also be indirect.
# One function can call a second, which calls the first,
# which calls the second, and so on.
def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x-1)


def is_odd(x):
    return not is_even(x)


print(is_odd(17))
print(is_even(23))


def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)


print(fib(4))
