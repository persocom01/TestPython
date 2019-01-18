# Prints the default file directory.
import os
print(os.getcwd())
# Changes default directory.
os.chdir(os.getcwd() + r'\TestPython/')

# Using with automatically closes the file when done.
# Otherwise, use of f.close() is needed or resources are wasted.
with open('file.txt', 'r') as f:
    print(f.read())

# Demonstrates use of readline to read individual lines.
# The b mode is necessary for use of most seek methods other than 0 to work.
with open('file.txt', 'rb') as f:
    print(f.readline())
    print(f.readline())
    # Demonstrates use of tell to read position and seek to goto position.
    print(f.tell())
    # For the second argument, 0=from beginning, 1=from current, 2=from end.
    print(f.seek(-8, 2))
    print(f.readline())

# Functionally idential to repeating readline() if you read all lines.
# readlines() returns a list of lines. Alternatively, use list(f).
with open('file.txt', 'r') as f:
    for line in f.readlines():
        print(line, end='')
    print()

# Demonstrates use of loops to read files instead of with.
# It does not close the file automatically.
try:
    f = open('file.txt', 'r')
    for line in f:
        print(line, end='')
finally:
    print(f.closed, '\n')
    f.close()

# Demonstrates writing to a file.
# Because changes won't be saved until the file is closed,
# it has to be closed before the new contents can be read.
# Not used in this file is the mode a for append.
try:
    f = open('file2.txt', 'w+')
    f.write('line1\nline2')
    # Reads nothing.
    print(f.read(), end='')
finally:
    f.close()
    f = open('file2.txt', 'r')
    print(f.read())
    f.close()
