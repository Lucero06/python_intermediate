def my_min(*args):
    return min(args)


print(my_min(8, 13, 4, 42, 120, 7))

nums = {1, 2, 3, 4, 5, 6}
nums = {0, 1, 2, 3} & nums
print(nums)


def power(x, y):
    if y == 0:
        return 1
    else:
        return x * power(x, y-1)


print(power(2, 3))

a = (lambda x: x*(x+1))(6)
print(a)

nums = [1, 2, 8, 3, 7]

res = list(filter(lambda x: x % 2 == 0, nums))

print(res)


def func(**kwargs):
    print(kwargs["zero"])


func(a=0, zero=8)


def spell(txt, i):
    # your code goes here
    i -= 1
    if (i >= 0):
        print(txt[i])
        return spell(txt, i)


txt = input()

spell(txt, len(txt))
