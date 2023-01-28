# This similarity can be expressed by making them all inherit from a superclass Animal,
# which contains the shared functionality.
# To inherit a class from another class,
# put the superclass name in parentheses after the class name.


# A class that inherits from another class is called a subclass.
# A class that is inherited from is called a superclass.

class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Cat(Animal):
    def purr(self):
        print("Purr...")


class Dog(Animal):
    def bark(self):
        print("Woof!")


fido = Dog("Fido", "brown")
print(fido.color)
fido.bark()


class Wolf:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Grr...")


class Dog(Wolf):
    def bark(self):
        print("Woof")


husky = Dog("Max", "grey")
husky.bark()

# super is a useful inheritance-related function that refers to the parent class.
# It can be used to find the method with a certain name
# in an object's superclass.


class A:
    def spam(self):
        print(1)


class B(A):
    def spam(self):
        print(2)
        super().spam()


B().spam()


# 1. Inherit the Rectangle class from Shape.
# 2. Define the perimeter() method in the Rectangle class,
# printing the perimeter of the rectangle.
class Shape:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        print(self.width*self.height)


class Rectangle(Shape):
    # your code goes here
    def perimeter(self):
        print(2 * (self.width+self.height))


w = int(input())
h = int(input())

r = Rectangle(w, h)
r.area()
r.perimeter()
