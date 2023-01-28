# Class methods are different -- they are called by a class,
# which is passed to the cls parameter of the method.

# A common use of these are factory methods,
# which instantiate an instance of a class,
# using different parameters than those usually passed to the class constructor.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    @classmethod
    def new_square(cls, side_length):
        return cls(side_length, side_length)


square = Rectangle.new_square(5)
print(square.calculate_area())


# Static methods behave like plain functions,
# except for the fact that you can call them from an instance of the class.
# Static methods are similar to class methods,
# except they don't receive any additional arguments;
# they are identical to normal functions that belong to a class.
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No pineapples!")
        else:
            return True


ingredients = ["cheese", "onions", "spam"]

print(Pizza.validate_topping("cheese"))
pizza = Pizza("cheese")
print(pizza.toppings)

if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)
print(pizza.toppings)


# The given code takes 2 numbers as input and calls the static area()
# method of the Shape class,
# to output the area of the shape,
# which is equal to the height multiplied by the width.
# your code goes here
class Shape:
    @staticmethod
    def area(w, h):
        return w*h


w = int(input())
h = int(input())

print(Shape.area(w, h))
