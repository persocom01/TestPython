import string

# Demonstrates various uses of f literal format string.
year = 2018
event = 'comiket'
# !r applies repr() to variable.
print(f'It\'s time for the {year} {event!r}.')
# <> alignment indicators. 10 is the occupied space size.
print(f'{year:<10} ==> {event:>10}')

# Demonstrates use of format() method.
participants = 1234567
prior_year = 987654
change = (participants - prior_year) / prior_year
# Possible to leave out 0 and 1 positional indicators in this case since
# the arguments are in the same order.
# + indicates that the sign will be displaced whether the figure is +ve or -ve.
# Alternative is ' ' (space) for leading space for +ve values.
# Default is -.
print('This year, there was a {0:+2.2%} change in particpants '
      'represented by {1:,} people.'
      .format(change, abs(participants - prior_year), ))

# A dictionary can be used to pass keyword arguments to the functionself.
# Keywords cannot be numerical.
franchises = {'AL': 2521, 'KC': 35123, 'FGO': 92346}
# This step is actually completely unnecessary since the print statement
# demonstrates format by keywords.
# What it does though, is rearranges the dictionary in order of largest value.
franchises = {x: franchises[x] for x in sorted(
    franchises, key=franchises.__getitem__)}
print('The top three franchise turnouts for  were'
      ' {FGO:,}, {KC:,} and {AL:,}\n'.format(**franchises))

# Demonstrates use of vars, which returns a dictionary of all local variables.
print(vars())
print('{__name__}\n{year}\n{event}\n'.format(**vars()))

# Demonstrates different ways to align a string.
print(str(year).ljust(10, '_'), event.center(10, '_'), end=' ')
print(str(participants).rjust(10, '_'))
print()

# Demonstrates use of templates in the string module.
# $ is used as a placeholder. $$ is needed to display $ normally.
t = string.Template('${animal}girls cost $$50 to $action.')
print(t.substitute(animal='racoon', action='pet'))
# safe substitute is used so incomplate arguments may be passed without error.
print(t.safe_substitute(animal='racoon'))

# The $ placeholder can be defined as something else.


class BatchRename(string.Template):
    delimiter = '?'


t = BatchRename('?{animal}girls cost ??50 to ?action.')
print(t.substitute(animal='racoon', action='pet'))
