# The function map takes a function and an iterable as arguments,
# and returns a new iterable with the function applied to each argument.
def add_five(x):
    return x + 5


nums = [11, 22, 33, 44, 55]
print(map(add_five, nums))
result = list(map(add_five, nums))
print(result)


# Lambda syntax.
nums = [11, 22, 33, 44, 55]
result = list(map(lambda x: x+5, nums))
print(result)


# map
# You work on a payroll program.
# Given a list of salaries, you need to take the bonus everybody is getting as input and increase all the salaries by that amount.
# Output the resulting list.
salaries = [2000, 1800, 3100, 4400, 1500]
bonus = int(input())
salaries = list(map(lambda x: x+bonus, salaries))
print(salaries)
