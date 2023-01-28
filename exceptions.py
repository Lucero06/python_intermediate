# ImportError: an import fails;
# IndexError: a list is indexed with an out-of-range number;
# NameError: an unknown variable is used;
# SyntaxError: the code can't be parsed properly;
# TypeError: a function is called on a value of an inappropriate type;
# ValueError: a function is called on a value of the correct type,
# but with an inappropriate value.
try:
    num1 = 7
    num2 = 0
    print(num1 / num2)
    print("Done calculation")
except ZeroDivisionError:
    print("An error occurred")
    print("due to zero division")

try:
    variable = 10
    print(variable + "hello")
    print(variable / 2)
except ZeroDivisionError:
    print("Divided by zero")
except (ValueError, TypeError):
    print("Error occurred")


try:
    print(1/0)
except ZeroDivisionError:
    print(4)
else:
    print(5)


def withdraw(amount):
    print(str(amount) + " withdrawn!")


# your code goes here
try:
    withdraw(int(input()))
except (ValueError):
    print("Please enter a number")


# In case the index is not valid, you should output "Item not found".
# In case the index is valid and the item name is output successfully,
# you should output "Thanks for your order".

menu = ['Fries', 'Sandwich', 'Cheeseburger', 'Coffee', 'Soda']
# your code goes here
n = input()
try:
    print(menu[int(n)])
    print("Thanks for your order")
except (IndexError, ValueError):
    print("Item not found")
