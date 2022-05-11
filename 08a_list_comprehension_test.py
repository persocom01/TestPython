# Demonstrates a way to generate lists without need for loops or lambdas.

# Demonstrates an if else comprehension.
# is_sevens = []
# for x in range(10):
#     if x == 7:
#         is_sevens.append('yes')
#     else:
#         is_sevens.append('no')
is_sevens = ['yes' if x == 7 else 'no' for x in range(10)]
print(is_sevens)

# Demonstrates multiple conditions using multiple if.
# Conditions are evaluated from left to right.
even_and_multiple_of_3_above_0 = [x for x in range(20) if x % 2 == 0 if x % 3 == 0 if x > 0]
print(even_and_multiple_of_3_above_0)

# Demonstrates basic filtering.
odds = [x for x in range(10) if x % 2 != 0]
print(odds)


# Variables or function that return boolean values are named is_var or has_var
# by convention.


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f+2) == 0:
            return False
        f += 6
    return True


# Demonstrates filtering of list using a function.
odds = [x for x in odds if is_prime(x)]
print(odds)


class C:
    def and_double(x):
        # Not using [] returns a tuple.
        return [x, x*2]


# Demonstrates usage of method on list and ability to create nested lists.
new_odds = [C.and_double(x) for x in odds]
print('method:', new_odds)
# An alternative to using list comprehensions to map is using the map function.
# It is said to use less memory.
odds = list(map(C.and_double, odds))
print('map:', odds)

# Demonstrates using a list comprehension to generate a nested list.
reversed_odds = [[y, x] for [x, y] in odds]
print('reversed:', reversed_odds)

# Demonstrates transposition of nested lists.
# zip is normally used on two seperate lists to make them one.
odds = list(zip(*odds))
print('zipped:', odds)

# Demonstrates unpacking of zipped list.
odds1, odds2, odds3 = zip(*odds)
print('unpacked:', odds1, odds2, odds3)

# Demonstrates falttening of list.
odds = [x for tuple in odds for x in tuple]
print('flat:', odds)

# Demonstrates deletion of part of list.
del odds[3:]
print('del:', odds)
