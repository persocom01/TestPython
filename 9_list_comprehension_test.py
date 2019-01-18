# Demonstrates a way to generate lists without need for loops or lambdas.
# odd = []
# for x in range(10):
#     if x%2 == 0:
#         odd.append(x)
odd = [x for x in range(10) if x % 2 != 0]
print(odd)


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


# Demonstrates filtering of list using function.
odd = [x for x in odd if is_prime(x) == True]
print(odd)


class C:
    def and_double(x):
        # Not using [] returns a tuple.
        return [x, x*2]


# Demonstrates usage of method on list and ability to create nested lists.
odd = [C.and_double(x) for x in odd]
print(odd)

# Demonstrates transposition of nested lists.
# zip is normally used on two seperate lists to make them one.
odd = list(zip(*odd))
print(odd)

# Demonstrates unpacking of zipped list.
odd1, odd2, odd3 = zip(*odd)
print(odd1, odd2, odd3)

# Demonstrates falttening of list.
odd = [x for y in odd for x in y]
print(odd)

# Demonstrates deletion of part of list.
del odd[3:]
print(odd)
