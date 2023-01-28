# Generators are a type of iterable, like lists or tuples.
# Unlike lists, they don't allow indexing with arbitrary indices,
# but they can still be iterated through with for loops.
# They can be created using functions and the yield statement.

# after each yield call not only the generator returns something
# but also remembers its state.
# Calling the next() method brings control back to the generator
# starting after the last executed yield statement.
# Each yield statement is executed only once,
# in the order it appears in the code.
# After all the yield statements have been executed iteration ends.
# Since generators support iterator protocol, they can be used in for loops.

# The yield statement is used to define a generator,
# replacing the return of a function to provide a result to its caller
# without destroying local variables.

def countdown():
    i = 5
    while i > 0:
        yield i
        i -= 1


r = countdown()
print(countdown())
print(list(countdown()))
print(r)
print(next(r))
print(next(r))
print(next(r))

print(r)
print(next(r))
print(list(r))

for i in countdown():
    print(i)
print(list(countdown()))
print(r)
print(list(r))

try:
    print(next(r))
except Exception as err:
    print(err)


def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i


print(list(numbers(11)))

n = numbers(11)
print(next(n))
print(next(n))


# Using generators results in improved performance,
# which is the result of the lazy (on demand) generation of values,
# which translates to lower memory usage.
# Furthermore, we do not need to wait until all the elements have been generated
# before we start to use them.
