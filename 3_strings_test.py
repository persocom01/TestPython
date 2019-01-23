texts = []

# Demonstrates \used to escape special characters as well as addition and
# multiplication.
texts = texts + ['spam said ' + 2*'\'eggs\'']

# Demonstrates r used to indicate rawtext as well as quoted string autojoin.
# Often used with regex.
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
slice_text = 'spam and eggs'
slices = [5, -7, len(slice_text) - 6, slice(0, 8)]

for s in slices:
    print(slice_text[s])

# Demonstrates list method insert.
insert_text = 'spam and eggs'
# Demonstrates splitting of a string into a list.
insert_text_list = insert_text.split(' ')
for i in insert_text_list:
    if 'spam' in i:
        # If the string inserted ahead of the searched string contains the
        # searched string, it results in an infinite loop.
        insert_text_list.insert(insert_text_list.index(i) + 1, 'ham')
# Prints list without commas.
print(*insert_text_list, '\n', sep=' ')

# Demonstrates common functions used on strings.
text = '_spam and eggs_'

# Case manipulation.
print(text.lower(), text.upper())
# Removes _ from front and back.
print(text.strip('_'))
# Tests if all of string is of type.
# Also demonstrates use of more than 1 function at a time.
# isupper and islower are also functions.
print(text.strip('_').isalpha(), text.isdigit(), text.isspace())
# Tests if string starts or ends with something.
print(text.startswith('spam'), text.endswith('_'))
# Replace part of string.
print(text.replace('spam', 'eggs'))
# Opposite of split.
print(' '.join(insert_text_list))
