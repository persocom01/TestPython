# Operators from highest to lowest prioirty:
# ()
# f(arg):
# slice[:9]
# list[index]
# var.method
# **

# Demonstrates use of conditions in variables.
# and and or are evaluated from left to right.
letter1, letter2, letter3 = 'a', '', 'c'
non_null = letter1 and letter2 and letter3
print(non_null)