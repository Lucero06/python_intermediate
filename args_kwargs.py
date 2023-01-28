# Using *args as a function parameter enables you to pass an arbitrary number of arguments
# to that function. The arguments are then accessible as the tuple args
# in the body of the function.

def function(named_arg, *args):
    print(named_arg)
    print(args)


function(1, 2, 3, 4, 5)

# The parameter *args must come after the named parameters to a function.
# The name args is just a convention; you can choose to use another.


# The keyword arguments return a dictionary
# in which the keys are the argument names,
# and the values are the argument values.
def my_func(x, y=7, *args, **kwargs):
    print(x)
    print(y)
    print(args)
    print(kwargs)
    print(kwargs['a'])
    print(kwargs['b'])


my_func(2, 3, 4, 5, 6, a=7, b=8)
