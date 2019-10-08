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

# Demonstrates use of the % operator to insert a %d int, %s string,
# and %.*f a float with * decimal places.
temperature_today = 'The temperature at %dpm in %s today was %.*f degrees Celcius.' % (
    5, 'Singapore', 2, 30.4267)
print(temperature_today)
print()

# Demonstrates different ways to slice a string.
# 5 is the 6th char from the front. -7 is the 7th char from the back.
# slice(start, stop, step) allows you to slice multiple chars at once.
slice_text = 'spam and eggs'
slices = [5, -7, len(slice_text) - 6, slice(0, 6)]

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
        # That's why you generally just create a new list instead of
        # Trying to modify existing ones.
        insert_text_list.insert(insert_text_list.index(i) + 1, 'ham')
# Prints list without commas.
print(*insert_text_list, '\n', sep=' ')

# Demonstrates common functions used on strings.
text = '_spam spam and eggs_'

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
# Replace all instances of a string inside a string with another.
print(text.replace('spam', 'eggs'))
# Opposite of split.
print(' '.join(insert_text_list))
# Returns index of first instance of substring in string.
# Returns -1 if substring is not found.
print(text.find('eggs'))
# It is possible to use index() instead of find.
# index returns ValueError if substring is not found.
# index() can be applied to lists as well.
print(text.index('eggs'))
