# You need to create a generator function primeGenerator(),
# that will take two numbers as arguments,
# and use the isPrime() function to output the prime numbers in the given range
# (between the two arguments).
def isPrime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    for n in range(2, x):
        if x % n == 0:
            return False
    return True


def primeGenerator(a, b):
    # your code goes here
    nums = list(range(a, b))
    for n in nums:
        if (isPrime(n)):
            yield n
    # with lambda:
    # primes = list(filter((lambda x: isPrime(x) == True), nums))
    # return primes


f = int(input())
t = int(input())

print(list(primeGenerator(f, t)))
