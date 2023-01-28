class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs


felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)

# Classes are created using the keyword class and an indented block,
# which contains class methods (which are functions).
# The __init__ method is the most important method in a class.
# This is called when an instance (object) of the class is created,
# using the class name as a function.
print(felix.color)


class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Woof!")


fido = Dog("Fido", "brown")
print(fido.name)
fido.bark()


class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def intro(self):
        print(self.name + " (Level " + self.level + ")")


# your code goes here
name = input()
level = input()
player = Player(str(name), str(level))
player.intro()
