# Demonstrates a way to generate lists without need for loops or lambdas.
# odd = []
# for x in range(10):
#     if x%2 == 0:
#         odd.append(x)
odd = [x for x in range(10) if x % 2 != 0]
print(odd)


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
odd = [x for x in odd if is_prime(x)]
print(odd)


class C:
    def and_double(x):
        # Not using [] returns a tuple.
        return [x, x*2]


# Demonstrates usage of method on list and ability to create nested lists.
odd = [C.and_double(x) for x in odd]
print(odd)

# Demonstrates using a list comprehension to generate a nested list.
reversed_odd = [[y, x] for [x, y] in odd]
print('reversed:', reversed_odd)

# Demonstrates transposition of nested lists.
# zip is normally used on two seperate lists to make them one.
odd = list(zip(*odd))
print('zipped:', odd)

# Demonstrates unpacking of zipped list.
odd1, odd2, odd3 = zip(*odd)
print('unpacked:', odd1, odd2, odd3)

# Demonstrates falttening of list.
odd = [x for tuple in odd for x in tuple]
print('flat:', odd)

# Demonstrates deletion of part of list.
del odd[3:]
print('del:', odd)
