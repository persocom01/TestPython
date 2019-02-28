import reprlib
import pprint
import textwrap
import locale

# reprlib is a version of repr() that limits the output displayed.
print('Normal repr:', repr(set('supercalifragilisticexpialidocious')))
print('reprlib:', reprlib.repr(set('supercalifragilisticexpialidocious')))
print()

# pprint is short for 'pretty print'. It can be better for nested lists.
# Other parameters exist, check online documentation.
basket = [[['apple', 'orange'], 'banana'], 'eggs', ['tuna', 'salmon']]
print(basket)
pprint.pprint(basket, indent=2, width=30)
print()

# Different ways of wraping text.
text = '''\
The quick brown fox jumps over the lazy dog.
However, the dog did not notice, as it was asleep.
The dog continued its peaceful slumber, and all was well.\
    '''
# repr is used here to show that fill uses \n to wrap text.
print(repr(textwrap.fill(text)))
# wrap returns a list of strings instead.
print(textwrap.wrap(text))
print()

# Demonstrates use of locale module.
# Sets locale to user default setting.
locale.setlocale(locale.LC_ALL, '')
conv = locale.localeconv()
print(conv)
x = 111000.5
format = '%s%.*f'.format
print(locale.format_string(
    format, (conv['int_curr_symbol'], conv['frac_digits'], x), grouping=True))
