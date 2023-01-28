# Properties provide a way of customizing access to instance attributes.
# when the instance attribute with the same name as the method is accessed,
# the method will be called instead.
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        try:
            self.pineapple_allowed = False  # no
        except Exception as e:
            print(e)

    @property
    def pineapple_allowed(self):
        return False  # yes


pizza = Pizza(["cheese", "tomato"])
print(pizza.toppings)
print(pizza.pineapple_allowed)  # yes
try:
    pizza.pineapple_allowed = True
except Exception as e:
    print(e)


class Person:

    def __init__(self, age):
        self.age = int(age)

    @property
    def isAdult(self):
        if self.age > 18:
            return True
        else:
            return False


p = Person(8)
print(p.isAdult)


# To define a setter, you need to use a decorator of the same name as the property,
# followed by a dot and the setter keyword.
# The same applies to defining getter functions.
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        self._pineapple_allowed = False

    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed

    @pineapple_allowed.setter
    def pineapple_allowed(self, value):
        if value:
            password = input("Enter the password: ")
            if password == "123":
                self._pineapple_allowed = value
            else:
                raise ValueError("Alert! Intruder!")


print("== Pizza 2")
pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza._pineapple_allowed = True  # but
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)


# need to add an isAlive property,
# which returns True if the lives count is greater than 0.
# Complete the code by adding the isAlive property.
class Player:
    def __init__(self, name, lives):
        self.name = name
        self._lives = lives

    def hit(self):
        self._lives -= 1

    # your code goes here
    @property
    def isAlive(self):
        if (self._lives > 0):
            return True


p = Player("Cyberpunk77", int(input()))
i = 1
while True:
    p.hit()
    print("Hit # " + str(i))
    i += 1
    if not p.isAlive:
        print("Game Over")
