# filter
# The function filter filters an iterable
# by leaving only the items that match a condition(also called a predicate).
nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x % 2 == 0, nums))
print(res)

# Like map, the result has to be explicitly converted to a list if you want to print it.
