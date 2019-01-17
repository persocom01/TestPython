def compare(x, y):
    try:
        if x == y:
            print(x, 'equals', y)
        elif x > y:
            print(x, 'greater than', y)
        elif x < y:
            print(x, 'smaller than', y)
    except TypeError:
        print(x, 'cannot be compared to', y)

list1 = [x for x in range(3)]
list2 = [0.0, 1, 2.0,]
tuple1 = (0, 1, 2,)
letter1 = ['ABC']
letter2 = ['abc']

compare(list1, list2)
compare(list1, tuple1)
compare(letter1, letter2)
