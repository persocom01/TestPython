texts = []

# Demonstrates \used to escape special characters as well as addition and multiplication.
texts = texts + ['spam said ' + 2*'\'eggs\'']

# Demonstrates r used to indicate rawtext as well as quoted string autojoin. Often used with regex.
texts.append(
    r'^spam\s[a-z]{3}'
    r'\seggs?')

# Demonstrates multiline string without \n. \ is needed to escape autonewline.
texts.append('''\
spam
and
eggs\
    ''')

for t in texts:
    print(t, '\n')

# Demonstrates different ways to slice a string.
slicetext = 'spam and eggs'
slices = [5, -7, len(slicetext) - 6, slice(0,8)]

for s in slices:
    print(slicetext[s])

# Demonstrates list method insert as well as print list without commas.
inserttext = ['spam ', 'and ', 'eggs']
for i in inserttext:
    if 'spam' in i:
        # If the code order is switched it doesn't work.
        # If the string inserted ahead of the searched string contains the searched string, it results in an infinite loop.
        inserttext.insert(inserttext.index(i) + 1, 'ham ')
        inserttext[inserttext.index(i)] = 'spam, '
print(*inserttext, sep='')
