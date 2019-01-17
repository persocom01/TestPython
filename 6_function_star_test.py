# An import to help inspect function parameters
from inspect import signature

# Demonstrates use of optional postional and keyword arguments
# ': str' and '-> str' are annotations.
# They specify what data types the function takes in and what it returns respectively.
# In this case, the function doesn't actually return anything, but annotations have effect on running the function.
def creature(kind, *args: str, HP=1, Atk, **kwargs) -> int:
    print('Name:', kind)
    # Counts if any optional positional arguments are given.
    if len(args) > 0:
        print('---Description---')
        for arg in args:
            print(arg)
    print('---Stats---')
    print('HP:', HP)
    # Counts if any optional keyword arguments are given.
    if len(kwargs) > 0:
        print('---Items---')
        for kw in kwargs:
            print(kw, kwargs[kw])
        print('Total items:', len(kwargs))
    # Alternative way to counts arguments.
    # The difference is more complicated specifications can be given.
    # In this case it counts number of keyword arguments without default values.
    sig = signature(creature)
    count = 0
    for param in sig.parameters.values():
        if param.kind == param.KEYWORD_ONLY and param.default is param.empty:
            count += 1
    print('No default =', count)

# Demonstrates uses of list/tuple as optional argument input.
description = ['A creature of the woods.',
        'Prefers ranged attacks.',]

# Demonstrates uses of dictionary as optional keyword argument input.
itemlist = ['Herb', 'Bow']
# Sorts list in alphabetical order.
itemlist.sort()
# Creates dictionary.
itemdic = {'item' + str(itemlist.index(item)+1) + ':': item for item in itemlist}

creature('Elf', *description,
        HP=100, Atk=10, **itemdic)
