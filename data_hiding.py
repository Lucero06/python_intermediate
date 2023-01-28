# encapsulation involves packaging of related variables and functions
# into a single easy-to-use object -- an instance of a class.
# A related concept is data hiding,
# which states that implementation details of a class should be hidden,
# and a clean standard interface be presented for those who want to use the class.
# there are no ways of enforcing that a method or attribute be strictly private.
# However, there are ways to discourage people from accessing parts of a class,
# such as by denoting that it is an implementation detail,
# and should be used at their own risk.

# Weakly private methods and attributes have a single underscore at the beginning.
# This signals that they are private, and shouldn't be used by external code.
# However, it is mostly only a convention,
# and does not stop external code from accessing them.


class Queue:
    def __init__(self, contents):
        self._hiddenlist = list(contents)

    def push(self, value):
        self._hiddenlist.insert(0, value)

    def pop(self):
        return self._hiddenlist.pop(-1)

    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)


queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)
# print(queue.hiddenlist)
# The __repr__ magic method is used for string representation of the instance.


# Strongly private methods and attributes have
# a double underscore at the beginning of their names.
# The purpose of this isn't to ensure that they are kept private,
# but to avoid bugs if there are subclasses that have methods
# or attributes with the same names.
class Spam:
    __egg = 7

    def print_egg(self):
        print(self.__egg)


s = Spam()
s.print_egg()  # yes
print(s._Spam__egg)  # yes
try:
    print(s.__egg)  # no
except Exception as e:
    print(e)
# The method __privatemethod of class Spam
# could be accessed externally with _Spam__privatemethod.


class Player:
    def __init__(self, name, lives, mana):
        self.name = name
        self._lives = lives
        self.__mana = mana
        self._salute = "hola"

    def hit(self):
        # your code goes here
        self._lives -= 1
        self.__mana -= 2
        if (self._lives == 0):
            print("Game Over")

    def __repr__(self):
        return "lives: {}, mana: {}, salute: {}"\
            .format(self._lives, self.__mana, self._salute)


p = Player("Cyberpunk77", 3, 0)
p.hit()
p.hit()
print(p._lives)
p.hit()
print(p._lives)
try:
    print(p.__mana)
except Exception as e:
    print(e)
    # but
    print(p._Player__mana)
print(p)


class Shooter(Player):

    def hit(self):
        self._lives -= 3
        try:
            self.__mana -= 1
        except Exception as e:
            print(e)
            # but
            self._Player__mana -= 1


s = Shooter("haha", 6, 10)
print(s._salute)
print(s._lives)
print(s._Player__mana)
s.hit()
print(s._lives)
print(s._Player__mana)
print(s)
