# Decorators provide a way to modify functions using other functions.
# This is ideal when you need to extend the functionality of functions
# that you don't want to modify.

def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap


def print_text():
    print("Hello world!")


decorated = decor(print_text)
decorated()
# We could say that the variable decorated is a decorated version of print_text

print_text = decor(print_text)
print_text()
# Now print_text corresponds to our decorated version.


# If we are defining a function we can "decorate" it with the @ symbol like:
@decor
def print_text():
    print("Hello world!")


print_text()
# A single function can have multiple decorators.
