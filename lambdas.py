def my_func(f, arg):
    return f(arg)


# lambda keyword followed by a list of arguments,
# a colon, and the expression to evaluate and return.
my_func(lambda x: 2*x*x, 5)

# named function


def polynomial(x):
    return x**2 + 5*x + 4


print(polynomial(-4))
# lambda
print((lambda x: x**2 + 5*x + 4)(-4))

# Functions created using the lambda syntax are known as anonymous.
